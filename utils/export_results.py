#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlsxwriter

def export_results (targets, ports_shodan, ports_censys, ports_onyphe, ports_binaryedge):
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    i = 0


    try:
        print ("\nExporting the results in an excel")
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('heinsenberg.xlsx')
        worksheet = workbook.add_worksheet()
        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})
        worksheet.write(row, col, "IP", bold)
        worksheet.write(row, col + 1, "Shodan", bold)
        worksheet.write(row, col + 2, "censys", bold)
        worksheet.write(row, col + 3, "onyphe", bold)
        worksheet.write(row, col + 4, "binaryedge", bold)
        row += 1
        # Iterate over the data and write it out row by row.

        for target in targets:
            col = 0
            worksheet.write(row, col, str(target))
            worksheet.write(row, col+1, str(ports_shodan[i]))
            worksheet.write(row, col+2, str(ports_censys[i]))
            worksheet.write(row, col+3, str(ports_onyphe[i]))
            worksheet.write(row, col+4, str(ports_binaryedge[i]))
            row += 1
            i +=1

        #Close the excel
        workbook.close()

    except Exception as exc:
        print ("Error in export_results " + str(exc))