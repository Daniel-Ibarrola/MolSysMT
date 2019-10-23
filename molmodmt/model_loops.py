
def add_loop (item, target_sequence=None, finesse=0, engine='modeller', verbose=False):

    from .multitool import get_form as _get_form, convert as _convert

    form_in = _get_form(item)

    if engine=='modeller':

        from molmodmt import sequence_alignment as _sequence_alignment
        import tempfile as _tempfile
        from os import remove as _remove
        from os import curdir as _curdir
        from os import listdir as _listdir
        from glob import glob
        import modeller as modeller
        import modeller.automodel as automodel
        from .multitool import get as _get, set as _set

        tmp_box = _get(item, box=True)

        seq_original = _convert(item, to_form='aminoacids1:seq')
        seq_aligned, _, _, _, _ = _sequence_alignment('aminoacids1:'+seq_original,
                                                      'aminoacids1:'+target_sequence)[0]

        tmp_pdbfilename = _tempfile.NamedTemporaryFile(suffix=".pdb").name
        tmp_name = tmp_pdbfilename.split('/')[-1].split('.')[0]
        tmp_seqfilename = '/tmp/'+tmp_name+'.seq'
        tmp_alifilename = '/tmp/'+tmp_name+'.ali'

        _convert(item, to_form=tmp_pdbfilename)

        if verbose:
            modeller.log.verbose()
        else:
            modeller.log.none()

        e = modeller.environ()
        e.io.atom_files_directory = ['.', '/tmp']
        m = modeller.model(e, file=tmp_pdbfilename)
        aln = modeller.alignment(e)
        aln.append_model(m, align_codes=tmp_name)
        aln.write(file=tmp_seqfilename)

        alifile = open(tmp_alifilename,'w')
        seqfile = open(tmp_seqfilename,'r')
        lines_seqfile = seqfile.readlines()
        alifile.write(lines_seqfile[1])
        alifile.write(lines_seqfile[2])
        alifile.write(seq_aligned+'*\n')
        alifile.write('>P1;'+tmp_name+'_fill\n')
        alifile.write('sequence:::::::::\n')
        alifile.write(target_sequence+'*\n')
        alifile.close()
        seqfile.close()
        del(lines_seqfile)

        a = automodel.loopmodel(e, alnfile = tmp_alifilename, knowns = tmp_name, sequence = tmp_name+'_fill')

        a.write_intermediates = False

        a.starting_model = 1
        a.ending_model = 1

        a.loop.starting_model = 1
        a.loop.ending_model = 12

        if finesse==0:
            a.loop.md_level = automodel.refine.very_fast
        elif finesse==1:
            a.loop.md_level = automodel.refine.fast
        elif finesse==2:
            a.loop.md_level = automodel.refine.slow
        elif finesse==3:
            a.loop.md_level = automodel.refine.very_slow
        elif finesse==4:
            a.loop.md_level = automodel.refine.slow_large

        a.make()

        _remove(tmp_pdbfilename)
        _remove(tmp_seqfilename)
        _remove(tmp_alifilename)

        files_produced = [ ff for ff in _listdir(_curdir) if ff.startswith(tmp_name) ]

        candidate_value = float("inf")
        candidate_pdb_file = None

        for pdb_loopmodel in [ ff for ff in files_produced if ff.startswith(tmp_name+'_fill.BL')]:
            pdb_file=open(pdb_loopmodel,'r')
            _ = pdb_file.readline()
            objective_function_value = float(pdb_file.readline().split(' ')[-1])
            if objective_function_value < candidate_value:
                candidate_value = objective_function_value
                candidate_pdb_file = pdb_loopmodel
            pdb_file.close()

        print("Best loop model with modeller's objective function:",candidate_value)
        tmp_item = _convert(candidate_pdb_file, to_form=form_in)

        for file_produced in files_produced:
            _remove(file_produced)

        _set(tmp_item, box=tmp_box)
        del(tmp_box)

        return tmp_item

    elif engine=='pyrosetta':
        pass

    elif engine=='ensembler':
        pass

