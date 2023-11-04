import os
import csv
input_folder = "input_folder"
output_folder = "output_folder"
result_file = "result_data.csv"
unique_ids = set()
combined_data = []
salaries = []
for filename in os.listdir(input_folder):
    if filename.endswith(".dat"):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, 'r') as datfile:
            reader = csv.reader(datfile, delimiter='\t')
            header = next(reader)
            for row in reader:
                if row[0] not in unique_ids:
                    unique_ids.add(row[0])
                    combined_data.append(row)
                    salaries.append(int(row[5]))
salaries.sort(reverse=True)
second_highest_salary = salaries[1]
total_salary = sum(salaries)
average_salary = total_salary / len(salaries)
output_path = os.path.join(output_folder, result_file)
with open(output_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    for row in combined_data:
        csv_writer.writerow(row)
    csv_writer.writerow([f"Second Highest Salary={second_highest_salary}", f"Average Salary={average_salary:.1f}"])
print(f"Combined data saved to {output_path}.")
