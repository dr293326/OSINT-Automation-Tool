from tkinter import *
from tkinter import messagebox
import SystemToolsManager
from src.HTTPServer import HTTPServer, prepare_html


class GUIModule:
    nmap_check_buttons = []
    vars = []
    input_fields = []
    names = [['TCP Connect', '-sT'], ['Stealth Connect', '-sS'], ['Xmas', '-sX'], ['FIN', '-sF'], ['ACK', '-sA'],
             ['NULL', '-sN']]
    search_engines = ['bing', 'google', 'hackertarget', 'netcraft', 'twitter', 'yahoo']
    harvester_check_buttons = []

    def __init__(self):
        outer_bg = "#696969"
        inner_bg = "#F4A201"

        root = Tk()
        # canvas = Canvas(root, height=400, width=700, bg='black')
        # canvas.pack()
        main_frame = Frame(root, height=400, width=700, bg=outer_bg)
        main_frame.pack(expand=True, fill='both')

        name_frame = Frame(main_frame, bg=inner_bg)
        name_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        name_label = Label(name_frame, text="Organization name:", bg=inner_bg, font=("Calibri", 12, "bold"), fg='white')
        name_label.place(relx=0.1, rely=0.25, relheight=0.5)
        name_entry = Entry(name_frame, bd=0)
        name_entry.place(relx=0.60, rely=0.25, relheight=0.5, relwidth=0.35)
        self.input_fields.append(name_entry)

        webpage_frame = Frame(main_frame, bg=inner_bg)
        webpage_frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)
        webpage_label = Label(webpage_frame, text="Main webpage address:", bg=inner_bg, font=("Calibri", 12, "bold"),
                              fg='white')
        webpage_label.place(relx=0.1, rely=0.25, relheight=0.5)
        webpage_entry = Entry(webpage_frame, bd=0)
        webpage_entry.place(relx=0.60, rely=0.25, relheight=0.5, relwidth=0.35)
        self.input_fields.append(webpage_entry)

        nmap_frame = Frame(main_frame, bg=inner_bg)
        nmap_frame.place(relx=0.1, rely=0.45, relwidth=0.39, relheight=0.3)
        nmap_label = Label(nmap_frame, text="Nmap port scanning option:", bg=inner_bg, font=("Calibri", 9, "bold"),
                           fg='white')
        nmap_label.place(relx=0.05, rely=0.05, relheight=0.2, relwidth=0.9)

        tcp = IntVar()
        nmap_check_button1 = Checkbutton(nmap_frame, text="TCP Connect", bg=inner_bg, font=("Calibri", 9, "bold"),
                                         activebackground=inner_bg, variable=tcp,
                                         command=lambda: self.deselect_others(nmap_check_button1,
                                                                              self.nmap_check_buttons))
        nmap_check_button1.config(highlightthickness=0)
        nmap_check_button1.place(relx=0.05, rely=0.25)
        self.nmap_check_buttons.append([nmap_check_button1, tcp])
        nmap_check_button1.select()

        stealth = IntVar()
        nmap_check_button2 = Checkbutton(nmap_frame, text="Stealth Connect", bg=inner_bg, font=("Calibri", 9, "bold"),
                                         activebackground=inner_bg, variable=stealth,
                                         command=lambda: self.deselect_others(nmap_check_button2,
                                                                              self.nmap_check_buttons))
        nmap_check_button2.config(highlightthickness=0)
        nmap_check_button2.place(relx=0.5, rely=0.25)
        self.nmap_check_buttons.append([nmap_check_button2, stealth])

        xmas = IntVar()
        nmap_check_button3 = Checkbutton(nmap_frame, text="Xmas", bg=inner_bg, font=("Calibri", 9, "bold"),
                                         activebackground=inner_bg, variable=xmas,
                                         command=lambda: self.deselect_others(nmap_check_button3,
                                                                              self.nmap_check_buttons))
        nmap_check_button3.config(highlightthickness=0)
        nmap_check_button3.place(relx=0.05, rely=0.5)
        self.nmap_check_buttons.append([nmap_check_button3, xmas])

        # nmap_check_button4 = Checkbutton(nmap_frame, text="TCP Connect", bg=inner_bg, font=("Calibri", 9, "bold"),
        #                                 activebackground=inner_bg)
        # nmap_check_button4.config(highlightthickness=0)
        # nmap_check_button4.place(relx=0.5, rely=0.5)
        # self.nmap_check_buttons.append(nmap_check_button4)

        fin = IntVar()
        nmap_check_button5 = Checkbutton(nmap_frame, text="FIN", bg=inner_bg, font=("Calibri", 9, "bold"),
                                         activebackground=inner_bg, variable=fin,
                                         command=lambda: self.deselect_others(nmap_check_button5,
                                                                              self.nmap_check_buttons))
        nmap_check_button5.config(highlightthickness=0)
        nmap_check_button5.place(relx=0.5, rely=0.5)
        self.nmap_check_buttons.append([nmap_check_button5, fin])

        ack = IntVar()
        nmap_check_button6 = Checkbutton(nmap_frame, text="ACK", bg=inner_bg, font=("Calibri", 9, "bold"),
                                         activebackground=inner_bg, variable=ack,
                                         command=lambda: self.deselect_others(nmap_check_button6,
                                                                              self.nmap_check_buttons))
        nmap_check_button6.config(highlightthickness=0)
        nmap_check_button6.place(relx=0.05, rely=0.75)
        self.nmap_check_buttons.append([nmap_check_button6, ack])

        null = IntVar()
        nmap_check_button7 = Checkbutton(nmap_frame, text="NULL", bg=inner_bg, font=("Calibri", 9, "bold"),
                                         activebackground=inner_bg, variable=null,
                                         command=lambda: self.deselect_others(nmap_check_button7,
                                                                              self.nmap_check_buttons))
        nmap_check_button7.config(highlightthickness=0)
        nmap_check_button7.place(relx=0.5, rely=0.75)
        self.nmap_check_buttons.append([nmap_check_button7, null])

        theHarvester_frame = Frame(main_frame, bg=inner_bg)
        theHarvester_frame.place(relx=0.51, rely=0.45, relwidth=0.39, relheight=0.3)
        theHarvester_label = Label(theHarvester_frame, text="theHarvester search engine:", bg=inner_bg,
                                   font=("Calibri", 9, "bold"),
                                   fg='white')
        theHarvester_label.place(relx=0.05, rely=0.05, relheight=0.2, relwidth=0.9)

        iter = 0
        row = 0
        column = 0
        for x in self.search_engines:
            var = IntVar()
            harvester_check_button = Checkbutton(theHarvester_frame, text=x, bg=inner_bg, font=("Calibri", 9, "bold"),
                                                 activebackground=inner_bg, variable=var)
            harvester_check_button.config(highlightthickness=0)

            if column == 0:
                harvester_check_button.place(relx=0.05, rely=0.25 + (row * 0.25))
            else:
                harvester_check_button.place(relx=0.5, rely=0.25 + (row * 0.25))

            self.harvester_check_buttons.append([harvester_check_button, var])
            harvester_check_button.config(
                command=lambda: self.deselect_others(self.get_selected_checkbutton_harvester(),
                                                     self.harvester_check_buttons))

            if column == 1 and row == 0:
                harvester_check_button.select()
                self.curr_harvester_opt = harvester_check_button

            if column == 0:
                column = 1
            else:
                column = 0
                row = row + 1
            iter = iter + 1

        button = Button(main_frame, text="Build report", bd=0, font=("Calibri", 12, "bold"), fg="white", bg=inner_bg,
                        activebackground="white", activeforeground=inner_bg, command=self.do_sth)
        button.place(relx=0.78, rely=0.9)

        root.mainloop()

    def deselect_others(self, checkbutton, checkbutton_list):

        for curr in checkbutton_list:

            if curr[0] == checkbutton and curr[1].get() == 1:
                for current in checkbutton_list:
                    if checkbutton != current[0]:
                        current[0].deselect()
                break

    def get_selected_checkbutton_harvester(self):
        for x in self.harvester_check_buttons:
            if x[1].get() == 1 and x[0] != self.curr_harvester_opt:
                self.curr_harvester_opt = x[0]
                return x[0]

    def validate_input(self):
        for x in self.input_fields:
            if x.get() == "":
                messagebox.showwarning('Warning', 'You need to fill the form correctly!')
                return -1
        return 0

    def translate_nmap_option(self, checkbutton_name):
        for x in self.names:
            if x[0] == checkbutton_name:
                return x[1]
        return ''

    def do_sth(self):
        if self.validate_input() == 0:
            # messagebox.showwarning('Warning', 'Report generation have been started! It might take a few minutes...'
            #                                   '\nPlease wait.')
            org_name = self.input_fields[0].get()
            website_address = self.input_fields[1].get()
            for x in self.nmap_check_buttons:
                if x[1].get() == 1:
                    nmap_scan_option = x[0]['text']

            ret = self.translate_nmap_option(nmap_scan_option)
            if ret == "":
                messagebox.showwarning('Error!', 'Critical error occurred!')
                print('Error: Critical error at do_sth in GUIModule')
            else:
                # NMAP
                result = SystemToolsManager.nmap('-oX - ' + website_address + ' ' + ret)
                nmap_result = SystemToolsManager.parse_nmap_xml_result(result)
                html_result = prepare_html(nmap_result=nmap_result)
                HTTPServer().open_report()

                # THE_HARVESTER
                # opt = self.curr_harvester_opt['text']
                # SystemToolsManager.the_harvester('-d ' + website_address + ' ' +
                #                                  '-l 100 -b ' + opt + ' -f harvest.xml')
                # result = SystemToolsManager.exec_command('cat', 'harvest.xml')
                # res = SystemToolsManager.parse_harvester_xml_result(result)
                # res.format_to_html()
                #
                # # SHODAN
                # shodan_result = SystemToolsManager.shodanAPI(website_address)
                # shodan_result_html = shodan_result.format_to_html()
                #
                # # SPIDERFOOT
                # spider_result_html = "<br><h3>SPIDERFOOT</h3><br><table><tr><th>Key</th><th>Value</th></tr>"
                # spider_result = SystemToolsManager.spiderfoot("-s " + website_address + " -t EMAILADDR -f -x -q -o json")
                # spider_result_html += SystemToolsManager.parse_spider_json_result(spider_result)
