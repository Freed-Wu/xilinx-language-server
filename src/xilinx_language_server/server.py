r"""Server
==========
"""
import json
import os
import re
from typing import Any, Literal, Tuple

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    Hover,
    MarkupContent,
    MarkupKind,
    Position,
    Range,
    TextDocumentPositionParams,
)
from pygls.server import LanguageServer


def check_extension(
    uri: str,
) -> Literal["vivado", "vitis"]:
    r"""Check extension.

    :param uri:
    :type uri: str
    :rtype: Literal["vivado", "vitis"]
    """
    if uri.split(os.path.extsep)[-1] == "xdc":
        return "vivado"
    return "vitis"


def get_document() -> dict[str, dict[str, str]]:
    r"""Get document.

    :rtype: dict[str, dict[str, str]]
    """
    path = os.path.join(
        os.path.join(os.path.dirname(__file__), "assets"), "json"
    )
    with open(os.path.join(path, "vivado.json"), "r") as f:
        vivado = json.load(f)
    with open(os.path.join(path, "xsct.json"), "r") as f:
        xsct = json.load(f)
    return {"vivado": vivado, "vitis": xsct}


class XilinxLanguageServer(LanguageServer):
    r"""Xilinx language server."""

    def __init__(self, *args: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :rtype: None
        """
        super().__init__(*args)
        self.document = get_document()

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            ext = check_extension(params.text_document.uri)
            word = self._cursor_word(
                params.text_document.uri, params.position, True
            )
            if not word:
                return None
            doc = self.document[ext].get(word[0])
            if not doc:
                return None
            return Hover(
                contents=MarkupContent(kind=MarkupKind.PlainText, value=doc),
                range=word[1],
            )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            ext = check_extension(params.text_document.uri)
            word = self._cursor_word(
                params.text_document.uri, params.position, False
            )
            token = "" if word is None else word[0]
            items = [
                CompletionItem(
                    label=x,
                    kind=CompletionItemKind.Function,
                    documentation=self.document[ext][x],
                    insert_text=x,
                )
                for x in self.document[ext]
                if x.startswith(token)
            ]
            return CompletionList(is_incomplete=False, items=items)

    def _cursor_line(self, uri: str, position: Position) -> str:
        r"""Cursor line.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :rtype: str
        """
        doc = self.workspace.get_document(uri)
        content = doc.source
        line = content.split("\n")[position.line]
        return str(line)

    def _cursor_word(
        self, uri: str, position: Position, include_all: bool = True
    ) -> Tuple[str, Range] | None:
        r"""Cursor word.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :param include_all:
        :type include_all: bool
        :rtype: Tuple[str, Range] | None
        """
        line = self._cursor_line(uri, position)
        cursor = position.character
        for m in re.finditer(r"\w+", line):
            end = m.end() if include_all else cursor
            if m.start() <= cursor <= m.end():
                word = (
                    line[m.start() : end],
                    Range(
                        start=Position(
                            line=position.line, character=m.start()
                        ),
                        end=Position(line=position.line, character=end),
                    ),
                )
                return word
        return None
