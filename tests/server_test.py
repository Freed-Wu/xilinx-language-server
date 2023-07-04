r"""Test server"""
from xilinx_language_server.server import get_document


class Test:
    r"""Test."""

    @staticmethod
    def test_get_document() -> None:
        r"""Test get document.

        :rtype: None
        """
        assert (
            len(
                get_document()["vivado"].get("create_project", "").splitlines()
            )
            > 1
        )
