import SystemToolsManager

html_result = SystemToolsManager.shodanAPI("8.8.8.8")
print("Saving to file")

f = open("test.html", "a")
f.write(html_result.format_to_html())
f.close()
