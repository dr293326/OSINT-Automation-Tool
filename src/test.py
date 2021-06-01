import json

import SystemToolsManager

result = SystemToolsManager.spiderfoot("-s umed.pl -t EMAILADDR -f -x -q -o json")
result_json = json.loads(result)
html_out = "<tr><td>E-mails:</td><td>"
for obj in result_json:
    html_out += obj['data'] + ", "
html_out += "</td></tr>"

f = open("test.html", "a")
f.write(html_out)
f.close()
