r"""Server
==========
"""

import json
import os
import re

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
from pygls.lsp.server import LanguageServer
from pygls.workspace.text_document import TextDocument


class XilinxLanguageServer(LanguageServer):
    r"""Xilinx language server."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.documents = {}
        path = os.path.join(os.path.dirname(__file__), "assets", "json")
        for filename in os.listdir(path):
            name = filename.split(".")[0]
            with open(os.path.join(path, filename)) as f:
                self.documents[name] = json.load(f)

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            doc = self.workspace.get_text_document(params.text_document.uri)
            filetype = self.get_filetype(doc)
            if not filetype:
                return None
            word = self._cursor_word(
                params.text_document.uri, params.position, True
            )
            if not word:
                return None
            doc = self.documents[filetype].get(word[0])
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
            doc = self.workspace.get_text_document(params.text_document.uri)
            filetype = self.get_filetype(doc)
            if not filetype:
                return CompletionList(is_incomplete=False, items=[])
            word = self._cursor_word(
                params.text_document.uri, params.position, False
            )
            token = "" if word is None else word[0]
            items = [
                CompletionItem(
                    label=x,
                    kind=CompletionItemKind.Function,
                    documentation=self.documents[filetype][x],
                    insert_text=x,
                )
                for x in self.documents[filetype]
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
        doc = self.workspace.get_text_document(uri)
        content = doc.source
        line = content.splitlines()[position.line]
        return str(line)

    def _cursor_word(
        self, uri: str, position: Position, include_all: bool = True
    ) -> tuple[str, Range] | None:
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

    @staticmethod
    def get_filetype(doc: TextDocument) -> str:
        ext = os.path.splitext(doc.path)[1]
        match ext:
            case ".xdc":
                return "vivado"
            case ".exp":
                return "expect"
        shebang = doc.source.splitlines()[0]
        if "vivado" in shebang:
            return "vivado"
        if "xsct" in shebang:
            return "vitis"
        if "expect" in shebang:
            return "expect"
        return ""
