from ...exceptions import ArgumentError
from ...variables import is_all

def digest_chain_name(chain_name, caller=None):
    """Checks if `chain_name` has the expected type and value.

    Parameters
    ----------
    chain_name : Any
        The `chain_name` argument for digestion.
    caller: str, optional
        Name of the function or method that is being digested.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/#the-any-type

    Returns
    -------
    bool
        Either True or False when caller is `get`.

    Raises
    -------
    ArgumentError
        If the given `chain_name` has not of the correct type or value.
    """

    if caller=='molsysmt.basic.get.get':
        if isinstance(chain_name, bool):
            return chain_name
    elif isinstance(chain_name, str):
        return chain_name

    raise ArgumentError('chain_name', value=chain_name, caller=caller, message=None)

