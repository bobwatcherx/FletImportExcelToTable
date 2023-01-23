from flet import *
import pandas as pd
import json


myexcel = pd.read_excel("percontohan.xlsx",sheet_name="Sheet1")
json_str = myexcel.to_json()
df = pd.read_json(json_str)

alldata = df.to_dict(orient="records")




def main(page:Page):
	datatable = DataTable(
		columns=[
		DataColumn(Text("name")),
		DataColumn(Text("age")),
		DataColumn(Text("address")),
		DataColumn(Text("actions")),
		],
		rows=[]

		)


	def showdata(e):
		# THEN PRINT YOU SELECT TO TERMINAL
		print(e.control.data.value)
	# PUSH EXCEL TO TABLE 

	for x in alldata:
		datatable.rows.append(
		DataRow(
			cells=[
			DataCell(Text(x['nama'])),
			DataCell(Text(x['age'])),
			DataCell(Text(x['address'])),
			DataCell(
			# AND IF YOU CLICK THE BUTTON THEN PRINT
			# YOU SELECTED DATA TO YOU TERMINAL
			ElevatedButton("Show select data",
			data=Text(f"you selected data : {x['nama']} - {x['age']} - {x['address']}"),
			on_click=lambda e:showdata(e)

			)



				),
			]

			)

		)



	page.add(
		Column([
		Text("Excel to TAble",size=30,weight="bold"),
		datatable	

		])

		)
flet.app(target=main)
