from fpdf import FPDF

from mosreg.schemas import Payment

def pdf_pattern_creation(pdf_path, ctr:Payment):
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()
    pdf.add_font("DejaVuSans", "", "fonts/DejaVuSerifCondensed.ttf", uni=True)
    pdf.set_font('DejaVuSans', '', 16)

    x = 50  # Adjust this value to shift the text to the right
    y = 10  # Y coordinate position
    text1 = "Генеральному директору"
    text2 = "ООО Газпром межрегионгаз Москва"
    text3 = "Тельнову О.В."
    text4 = "от_____________________"
    text5 = "Уважаемый Олег Владимрович!"
    text6 = f"Прошу Вас оплату по счету № {ctr.num} от {ctr.date}"
    text7 = f"считать оплатой за газ по договору № {ctr.contract}."
    text8 = "Руководитель организации _______________________"

    pdf.cell(100)
    pdf.cell(x, y, txt=text1, border=0, ln=1)
    pdf.cell(100)
    pdf.cell(x, y, txt=text2, border=0, ln=1)
    pdf.cell(100)
    pdf.cell(x, y, txt=text3, border=0, ln=1)
    pdf.cell(100)
    pdf.cell(x, y, txt=text4, border=0, ln=1)
    pdf.cell(100)
    pdf.cell(10, 40, txt=' ', border=0, ln=1)
    pdf.cell(100)
    pdf.cell(1, 10, txt=text5, border=0, align='C', ln=1)
    pdf.cell(100)
    pdf.cell(10, 5, txt=' ', border=0, ln=1)
    pdf.cell(100)
    pdf.cell(1, 10, txt=text6, border=0, align='C', ln=1)
    pdf.cell(100)
    pdf.cell(28, 10, txt=text7, border=0, align='R', ln=1)
    pdf.cell(100)
    pdf.cell(10, 30, txt=' ', border=0, ln=1)
    pdf.cell(100)
    pdf.cell(1, 10, txt=text8, border=0, align='C', ln=1)
 

    pdf.output(pdf_path)

