from datasets import load_dataset

dataset = load_dataset("wikipedia", "20220301.simple")

# Modify this to retrieve more data points
page_names = ["Earth"]

# Filter dataset to include only samples where the title is exactly the name of what is in the list.
# Eg. Retrieve only "Earth" and not "Earth Day"
filtered_data = [example for example in dataset["train"] if example["title"] in page_names 
                 and len(example["title"]) == len(page_names[page_names.index(example["title"])])]


# Writing to a .txt file for cleaning first
with open("output1.txt", "w") as file:
    file.write(str(filtered_data[0]["text"]))


