from smartphone import Smartphone

catalog = []
catalog.append(Smartphone(mark="Iphone", model="15 pro max", AbNumber="+79111111111"))
catalog.append(Smartphone(mark="POCO", model="X5 pro 5G", AbNumber="+79222222222"))
catalog.append(Smartphone(mark="Samsung", model="Galaxy S24 ultra", AbNumber="+79333333333"))
catalog.append(Smartphone(mark="Xiaomi", model="redmi 5s", AbNumber="+79444444444"))
catalog.append(Smartphone(mark="Sony Ericsson", model="w810i", AbNumber="+79444444444"))

for item in catalog:
    print(f"{item.mark} - {item.model}. {item.AbNumber}")
