import sys
import first_report
import second_report

extract = sys.arfv[1]
report_selection = sys.argv[2]

if report_selection == "First_Report":
    first_report.generate_first_report(extract)
elif report_selection == "Second_Report":
    second_report.generate_second_report(extract)
