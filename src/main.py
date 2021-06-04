from datetime import datetime

from IPython.terminal.pt_inputhooks.asyncio import loop

import SystemToolsManager
from GUIModule import GUIModule
from HTTPServer import HTTPServer
# from src.SystemToolsManager import exec_command, virustotal

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GUIModule()
    # virustotal_result = SystemToolsManager.virustotal('umed.pl')
    # for x in virustotal_result.public_key:
    #     print(x)
    #     # print(virustotal_result.popularity_ranks_list[x]['rank'])
    #     # print(datetime.fromtimestamp(virustotal_result.popularity_ranks_list[x]['timestamp']))
