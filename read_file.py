import json

with open('product_feat.json', 'rt') as rf:
  for line in rf:
    es_product_data = {
      '_index': 'thrive_rerank_features',
      '_type': 'doc'
    }
    product = json.loads(line)
    with open('rerank_features_index_source.ndjson', 'a') as wf:
      es_product_data['_id'] = product['productid']
      product['id'] = product.pop('productid')
      product['order_num'] = int(product['order_num'])
      product['search_add_num'] = int(product['search_add_num'])
      es_product_data['_source'] = product
      wf.write(json.dumps(es_product_data) +'\n')



  