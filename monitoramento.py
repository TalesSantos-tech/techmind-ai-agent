import psutil


def obter_cpu():
    return psutil.cpu_percent(interval=1)


def obter_ram():
    return psutil.virtual_memory().percent

import platform

def obter_temperatura_cpu():

    try:
        temps = psutil.sensors_temperatures()

        if temps:
            valores = []

            for _, sensores in temps.items():
                for s in sensores:
                    if s.current:
                        valores.append(s.current)

            if valores:
                return round(max(valores), 1)

    except:
        pass

    try:
        cpu_usage = psutil.cpu_percent(interval=0.5)

        # estimativa baseada em carga (não é temperatura real, mas útil)
        temp_estimativa = 30 + (cpu_usage * 0.5)

        return round(temp_estimativa, 1)

    except:
        pass

    return 0