"""Swap cyan/magenta across write/read/render."""

SWAP_ON_WRITE = False
SWAP_ON_READ = False
SWAP_ON_DETAIL = False
SWAP_ON_LIST = False


def assemble(cyan: float, magenta: float) -> tuple[float, float]:
    return (magenta, cyan) if SWAP_ON_WRITE else (cyan, magenta)


def project(cyan: float, magenta: float) -> tuple[float, float]:
    return (magenta, cyan) if SWAP_ON_READ else (cyan, magenta)


def detail_pair(cyan: float, magenta: float) -> tuple[float, float]:
    return (magenta, cyan) if SWAP_ON_DETAIL else (cyan, magenta)


def list_pair(cyan: float, magenta: float) -> tuple[float, float]:
    return (magenta, cyan) if SWAP_ON_LIST else (cyan, magenta)
