from pyscript import document, display

def calculate(event):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    sci = float(document.getElementById("sci").value)
    math = float(document.getElementById("math").value)
    eng = float(document.getElementById("eng").value)
    fil = float(document.getElementById("fil").value)
    ict = float(document.getElementById("ict").value)
    pe = float(document.getElementById("pe").value)

    gwa = (sci + math + eng + fil + ict + pe) / 6

    message = f"""
    Student: {fname} {lname}<br>
    <b>Grades:</b><br>
    Science: {sci}<br>
    Math: {math}<br>
    English: {eng}<br>
    Filipino: {fil}<br>
    ICT: {ict}<br>
    PE: {pe}<br><br>
    <b>General Weighted Average (GWA): {gwa:.2f}</b>
    """

    display(message, target="output", append=False)












