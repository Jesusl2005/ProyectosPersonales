import PySimpleGUI as sg

def run():
    Layout1 = [
        [sg.Text('BIENVENIDO A LA CALCULADORA DE INTERES')],
        [sg.Text('Usuario'), sg.Combo(['Jesus David Lopez', 'Julio Alfredo Lopez', 'Julio Andres Lopez'], key='-USUARIO-', default_value='Jesus David Lopez')],
        [sg.Button('Ingresar'), sg.Button('Salir')]
    ]
    window1 = sg.Window('INGRESO USUARIO', Layout1, element_justification='center')
    while True:
        event, values = window1.read()
        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        elif event == 'Ingresar':
            name = values['-USUARIO-']
            name = name.upper()
            window1.close()
            Layout2 = [
                [sg.Text(f'CALCULEMOS LOS INTERESES {name}')],
                [sg.Text('Ingresa el monto:'), sg.Input(justification='center',key='-MONTO-', pad=((128,0),0))],
                [sg.Text('Ingrese la tasa de interes mensual:'), sg.Input(justification='center',key='-TASA_INTERES-', pad=((25,0),0))],
                [sg.Text('Ingrese la duracion:'), sg.Input(justification='center',key='-TIEMPO-', pad=((115,0),0)), sg.Combo(('Dias', 'Quincenas', 'Meses', 'Años'),key='-PERIODO-')],
                [sg.Button('Calcular', pad=((250,10),5)), sg.Button('Limpiar')],
                [sg.Text('INGRESADO', justification='center'), sg.Text('RESULTADO', justification='center', pad=((250,20),5))],
                [sg.Text('Monto prestado: '), sg.Text('$0', key='-RMONTO-', pad=((19,10),5)),sg.Text('Interes total generado: '), sg.Text('$0', key='-INTERESTOTAL-')],
                [sg.Text('Tasa de interes: '), sg.Text('0%', key='-RTASA_INTERES-', pad=((20,10),5)),sg.Text('Valor total del credito: '), sg.Text('$0', key='-VALORCREDITO-')],
                [sg.Text('Numero de cuotas: '), sg.Text('0', key='-RTIEMPO-'),sg.Text('Valor de la cuota: '), sg.Text('$0', key='-CUOTA-')],
                [sg.Button('Finalizar', pad=((280,20),10))]
            ]
            window2 = sg.Window('CALCULADORA DE INTERESES', Layout2)
            while True:
                event2, values2 = window2.read()
                if event2 == 'Limpiar':
                    window2['-INTERESTOTAL-'].update('$0')
                    window2['-VALORCREDITO-'].update('$0')
                    window2['-CUOTA-'].update('$0')
                    window2['-TIEMPO-'].update('')
                    window2['-PERIODO-'].update('')
                    window2['-MONTO-'].update('')
                    window2['-TASA_INTERES-'].update('')
                    window2['-RMONTO-'].update('$0')
                    window2['-RTASA_INTERES-'].update('0%')
                    window2['-RTIEMPO-'].update('0')
                if event2 == sg.WIN_CLOSED or event2 == 'Finalizar':
                    break
                if event2 == 'Calcular':
                    monto = (values2['-MONTO-'])
                    t_interes = (values2['-TASA_INTERES-'])
                    tiempo = (values2['-TIEMPO-'])
                    monto = int(monto)
                    t_interes = float(t_interes)
                    tiempo = int(tiempo)
                    monto = '${:,.0f}'.format(monto)
                    t_interes = '{:,.2f}%'.format(t_interes)
                    window2['-RMONTO-'].update(monto)
                    window2['-RTASA_INTERES-'].update(t_interes)
                    window2['-RTIEMPO-'].update(tiempo)
                    if values2['-PERIODO-'] == 'Dias':
                        interesTotal = float(values2['-MONTO-'])*(float(values2['-TASA_INTERES-'])/100)*(float(values2['-TIEMPO-'])/30)
                        valorCredito = interesTotal + float(values2['-MONTO-'])
                        cuotas = valorCredito/float(values2['-TIEMPO-'])
                        interesTotal = '${:,.0f}'.format(interesTotal)
                        valorCredito = '${:,.0f}'.format(valorCredito)
                        cuotas = '${:,.0f}'.format(cuotas)
                        window2['-INTERESTOTAL-'].update(interesTotal)
                        window2['-VALORCREDITO-'].update(valorCredito)
                        window2['-CUOTA-'].update(cuotas)
                    elif values2['-PERIODO-'] == 'Quincenas':
                        interesTotal = float(values2['-MONTO-'])*(float(values2['-TASA_INTERES-'])/100)*(float(values2['-TIEMPO-'])/15)
                        valorCredito = interesTotal + float(values2['-MONTO-'])
                        cuotas = valorCredito/float(values2['-TIEMPO-'])
                        interesTotal = '${:,.0f}'.format(interesTotal)
                        valorCredito = '${:,.0f}'.format(valorCredito)
                        cuotas = '${:,.0f}'.format(cuotas)
                        window2['-INTERESTOTAL-'].update(interesTotal)
                        window2['-VALORCREDITO-'].update(valorCredito)
                        window2['-CUOTA-'].update(cuotas)
                    elif values2['-PERIODO-'] == 'Meses':
                        interesTotal = float(values2['-MONTO-'])*(float(values2['-TASA_INTERES-'])/100)*(float(values2['-TIEMPO-']))
                        valorCredito = interesTotal + float(values2['-MONTO-'])
                        cuotas = valorCredito/float(values2['-TIEMPO-'])
                        interesTotal = '${:,.0f}'.format(interesTotal)
                        valorCredito = '${:,.0f}'.format(valorCredito)
                        cuotas = '${:,.0f}'.format(cuotas)
                        window2['-INTERESTOTAL-'].update(interesTotal)
                        window2['-VALORCREDITO-'].update(valorCredito)
                        window2['-CUOTA-'].update(cuotas)
                    elif values2['-PERIODO-'] == 'Años':
                        interesTotal = float(values2['-MONTO-'])*(float(values2['-TASA_INTERES-'])/100)*(float(values2['-TIEMPO-'])*12)
                        valorCredito = interesTotal + float(values2['-MONTO-'])
                        cuotas = valorCredito/float(values2['-TIEMPO-'])
                        interesTotal = '${:,.0f}'.format(interesTotal)
                        valorCredito = '${:,.0f}'.format(valorCredito)
                        cuotas = '${:,.0f}'.format(cuotas)
                        window2['-INTERESTOTAL-'].update(interesTotal)
                        window2['-VALORCREDITO-'].update(valorCredito)
                        window2['-CUOTA-'].update(cuotas)
            window2.close()
            window1.close()
            exit()
if __name__ == '__main__':
    run()
