from data_collection import DataCollection
from data_to_sheet import UploadData

data_collection = DataCollection()
upload_data = UploadData()

try:
    for i in range(len(data_collection.property_addresses)):

        # get data and fill form automatically
        upload_data.house_data_upload(
            data_collection.property_addresses[i],
            data_collection.price_list[i],
            data_collection.address_links[i],
        )
except Exception as e:
    print('exception:', e)
