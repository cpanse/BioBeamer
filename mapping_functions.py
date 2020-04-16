import os
import re
from datetime import date

def map_data_G2HD_2(path, logger):
    """
    input: '\\\\fgcz-biobeamer.fgcz-net.unizh.ch\\Data2San\\20190206HM_11728_C6CYS.raw\\_PROC003.SIG'
    '\\\\fgcz-biobeamer.fgcz-net.unizh.ch\\Data2San\\p65\\Proteomics\\G2HD_2\\schesnov_20190101\\20190104HM_11622_C6.raw\\_PROC002.MAX'

    output: p65/Proteomics/G2HD_2/schesnov_20190000
    """

    pattern_dest = "^(\\\\\\\\fgcz-biobeamer.uzh.ch\\\\Data2San\\\\p[0-9]{1,4}\\\\[A-Za-z]{1,20}\\\\[A-Z0-9_]+)(\.PRO\\\\Data\\\\)([0-9]{8,8})(.+)$"
    regex_dest = re.compile(pattern_dest)
    match_dest = regex_dest.match(path)

    if match_dest:
        mg_path = match_dest.group(1)
        mg_date = match_dest.group(3)
        mg_folder = match_dest.group(4)


        path = os.path.normpath(
            "{path}\\analytic_{date}\\{date}{folder}".format(
                path=mg_path, date=mg_date, folder=mg_folder))
        return path
    else:
        logger.error('Could not apply mapping function. Raising exception')
        raise ValueError('Could not apply mapping function')
    return None


def map_data_analyst_tripletof_1(path, logger):
    """
    input:  'p1000/Data/selevsek_20150119'
    output: 'p1000/Proteomics/TRIPLETOF_1/selevsek_20150119'
    """

    pattern = ".*(p[0-9]+)\\\\Data\\\\([-0-9a-zA-Z_\\\.]+)$"
    regex = re.compile(pattern)
    match = regex.match(path)

    if match:
        return os.path.normpath("{0}/Proteomics/TRIPLETOF_1/{1}".format(match.group(1), match.group(2)))
    else:
        logger.error('Could not apply mapping function. Raising exception')
        raise ValueError('Could not apply mapping function')
    return None


def map_data_analyst_qtrap_1(path, logger):
    """
    input:  'p1000/Data/selevsek_20150119'
    output: 'p1000/Proteomics/TRIPLETOF_1/selevsek_20150119'
    """
    pattern = "(.*p[0-9]+)\\\\Data\\\\([-0-9a-zA-Z_\\\.]+)$"
    regex = re.compile(pattern)
    match = regex.match(path)

    if match:
        res = "{0}\\Proteomics\\QTRAP_1\\{1}".format(match.group(1), match.group(2))
        return res
    else:
        logger.error('Could not apply mapping function. Raising exception')
        raise ValueError('Could not apply mapping function')
    return None


def test_mapping_function(logger):
    '''
    Test mapping
    :return: nil
    '''
    tmp = '\\\\130.60.81.21\\Data2San\\p1001\\Data\\selevsek_20150119\\testdumm.raw'
    tmp2 = '\\\\130.60.81.21\\Data2San\\p1001\\Data\\selevsek_20150119\\testdumm2.wiff'
    tmp_ = map_data_analyst_qtrap_1(tmp, logger)
    if tmp_ != 'p1001\\Proteomics\\QTRAP_1\\selevsek_20150119\\testdumm.raw':
        print("mapping failed")
    tmp2_ = map_data_analyst_qtrap_1(tmp2, logger)
    if tmp2_ != 'p1001\\Proteomics\\QTRAP_1\\selevsek_20150119\\testdumm2.wiff':
        print("mapping failed")
