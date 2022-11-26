from parser import array_books
import xlsxwriter


def write_exel(parameter):
    workbook = xlsxwriter.Workbook('Books.xlsx')
    worksheet = workbook.add_worksheet('Книги')

    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '$#,##0'})

    worksheet.write('A1', 'Автор', bold)
    worksheet.write('B1', 'Название книги', bold)
    worksheet.write('C1', 'Цена', bold)
    worksheet.write('D1', 'Жанр', bold)
    worksheet.write('E1', 'Издательство', bold)
    worksheet.write('F1', 'Аннотация', bold)

    row = 1
    col = 0

    for item in parameter():
        worksheet.write(row, col, item[0])
        worksheet.write(row, col + 1, item[1])
        worksheet.write(row, col + 2, item[2], money)
        worksheet.write(row, col + 3, item[3])
        worksheet.write(row, col + 4, item[4])
        worksheet.write(row, col + 5, item[5])
        row += 1

    workbook.close()

write_exel(array_books)