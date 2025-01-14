from molsysmt._private.exceptions import ArgumentError

def digest_comparison(comparison, rule, caller=None):


    if caller == 'molsysmt.basic.compare.compare.compare':

        from molsysmt.basic.compare.compare import dict_compare_eq, dict_compare_in

        if rule == 'A_eq_B':
            if comparison.lower() in dict_compare_eq:
                return comparison.lower()

        elif rule in ['A_in_B', 'B_in_A']:
            if comparison.lower() in dict_compare_in:
                return comparison.lower()

    raise ArgumentError('comparison', value=comparison, caller=caller, message=None)
