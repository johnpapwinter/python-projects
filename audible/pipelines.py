from itemadapter import ItemAdapter


class AudiblePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == 'length':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace("Length:", "").strip()
            if field_name == 'release_date':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace("Release date:", "").replace("\n", "").strip()
            if field_name == 'language':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace("Language:", "").replace("\n", "").strip()
            if field_name == 'price':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace("\n", "").strip()

        return item
