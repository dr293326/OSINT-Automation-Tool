from datetime import datetime

from IPython.terminal.pt_inputhooks.asyncio import loop

import SystemToolsManager
from GUIModule import GUIModule
from HTTPServer import HTTPServer
# from src.SystemToolsManager import exec_command, virustotal

# Press the green button in the gutter to run the script.
from src.data.ShodanResult import ShodanResult

if __name__ == '__main__':
    GUIModule()
    # test = ShodanResult()
    # virustotal_result = SystemToolsManager.virustotal('umed.pl')
    # for x in virustotal_result.popularity_ranks_list:
    #     # print(x)
    #     print(virustotal_result.popularity_ranks_list[x]['rank'])
    #     print(virustotal_result.popularity_ranks_list[x]['timestamp'])
