#!flask/bin/python
from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

tasks = [
  {
    "id": "a877aad8-7854-411c-911c-52cd2f15bc7e",
    "picture": "http://placehold.it/128x128",
    "title": "elit qui qui aliquip ex incididunt",
    "createdAt": "Fri Aug 28 2015 10:27:41 GMT+0200 (CEST)",
    "creator": {
      "id": "1fed0c2b-374a-4c61-8e30-b6e16fdb2606",
      "name": "Kelly Mullins"
    }
  },
  {
    "id": "1a9a9589-29c8-4eaa-b94e-72320c1dbba2",
    "picture": "http://placehold.it/128x128",
    "title": "nisi ad fugiat eiusmod anim ipsum",
    "createdAt": "Fri Jul 04 2014 23:27:08 GMT+0200 (CEST)",
    "creator": {
      "id": "bec3588a-946a-4980-8570-44a34a3a056b",
      "name": "Barbara Burke"
    }
  },
  {
    "id": "0f23dc88-bcb0-4875-a237-f00366fc3e5b",
    "picture": "http://placehold.it/128x128",
    "title": "proident aute adipisicing eiusmod eiusmod ipsum",
    "createdAt": "Wed Aug 17 2016 02:25:44 GMT+0200 (CEST)",
    "creator": {
      "id": "42bdb10d-3200-4fc1-98de-c61b8127763d",
      "name": "Landry Rose"
    }
  },
  {
    "id": "7d3ebee7-d1cd-4e8d-bb3a-ec4f422179c7",
    "picture": "http://placehold.it/128x128",
    "title": "excepteur voluptate pariatur amet adipisicing est",
    "createdAt": "Thu May 22 2014 11:18:12 GMT+0200 (CEST)",
    "creator": {
      "id": "133c030a-ff18-4164-889f-1b79335e1555",
      "name": "Sweet Pratt"
    }
  },
  {
    "id": "abd89b82-a15b-4ed9-8ab1-bef2956e67c9",
    "picture": "http://placehold.it/128x128",
    "title": "esse ea aliquip ipsum ea eu",
    "createdAt": "Fri Dec 26 2014 05:55:46 GMT+0100 (CET)",
    "creator": {
      "id": "bb53dec0-1fa8-4b6f-98e0-7ac16c1d5948",
      "name": "Mcgowan Garcia"
    }
  },
  {
    "id": "c06df001-a06f-4119-a335-9fe63452c798",
    "picture": "http://placehold.it/128x128",
    "title": "incididunt occaecat tempor cillum proident irure",
    "createdAt": "Sun Mar 22 2015 20:50:55 GMT+0100 (CET)",
    "creator": {
      "id": "b46d1aa3-0230-4823-81fa-91b0c1454cb7",
      "name": "Robles Mason"
    }
  },
  {
    "id": "d01511d6-4775-4597-9996-1c988014119a",
    "picture": "http://placehold.it/128x128",
    "title": "incididunt laboris dolore sit commodo consectetur",
    "createdAt": "Sun Jan 01 2017 21:14:07 GMT+0100 (CET)",
    "creator": {
      "id": "8ad911d3-3b6f-41a1-a15b-5d432a5e7a7a",
      "name": "Garrett Dawson"
    }
  },
  {
    "id": "8b3870a8-b3ad-4c13-aa10-d6e6e7368cc2",
    "picture": "http://placehold.it/128x128",
    "title": "reprehenderit elit ipsum cillum nostrud laboris",
    "createdAt": "Sat Nov 21 2015 02:11:03 GMT+0100 (CET)",
    "creator": {
      "id": "cb55f236-9999-4df1-ba6e-0544d291ac00",
      "name": "Boyd Mcdonald"
    }
  },
  {
    "id": "74af47c6-225d-4f78-a7d8-597615604faa",
    "picture": "http://placehold.it/128x128",
    "title": "et aute est nulla cillum ipsum",
    "createdAt": "Fri Jul 10 2015 15:42:10 GMT+0200 (CEST)",
    "creator": {
      "id": "f79b9418-9a8e-43f5-9c44-7f4d34d915e7",
      "name": "Noreen Graves"
    }
  },
  {
    "id": "9a85ca1c-5746-4cf1-bf80-4d38d1521f8d",
    "picture": "http://placehold.it/128x128",
    "title": "duis mollit fugiat consequat non elit",
    "createdAt": "Thu Feb 05 2015 10:55:16 GMT+0100 (CET)",
    "creator": {
      "id": "b476ac74-5aa6-4e91-88ff-5f9975be1f25",
      "name": "Marietta Soto"
    }
  },
  {
    "id": "22011ddb-a9ba-425d-8209-d03751341e36",
    "picture": "http://placehold.it/128x128",
    "title": "sint sit sunt adipisicing irure sit",
    "createdAt": "Wed Nov 09 2016 23:36:07 GMT+0100 (CET)",
    "creator": {
      "id": "ae1ce72b-6370-41b5-b143-c2d802c079db",
      "name": "Maritza Castro"
    }
  },
  {
    "id": "4c86aa21-3633-4dae-9c2a-10bd3e7dac6b",
    "picture": "http://placehold.it/128x128",
    "title": "elit dolore eiusmod ullamco nisi aliqua",
    "createdAt": "Sat Mar 07 2015 02:15:22 GMT+0100 (CET)",
    "creator": {
      "id": "c9dde5ff-ede7-4f09-bf81-ff2980ff2f75",
      "name": "Hyde Rich"
    }
  },
  {
    "id": "ca200bba-8318-4c15-b2fa-f4f139229e2b",
    "picture": "http://placehold.it/128x128",
    "title": "elit sint tempor aliquip amet eiusmod",
    "createdAt": "Sun Feb 05 2017 01:07:11 GMT+0100 (CET)",
    "creator": {
      "id": "c1dae5d5-d455-4aa4-9e4e-3284abd0b6ca",
      "name": "Waters Mills"
    }
  },
  {
    "id": "ea0701f2-c95c-4011-b3d6-90f0b37b720b",
    "picture": "http://placehold.it/128x128",
    "title": "tempor ea qui consequat reprehenderit est",
    "createdAt": "Sat Feb 11 2017 10:47:40 GMT+0100 (CET)",
    "creator": {
      "id": "deb31bba-e62c-4bdb-9386-c42fcb4b06a1",
      "name": "Julia Hunt"
    }
  },
  {
    "id": "37e166a3-2238-4011-b486-b4beecd6e89c",
    "picture": "http://placehold.it/128x128",
    "title": "eu ad aliquip eiusmod in qui",
    "createdAt": "Tue Jul 07 2015 00:41:17 GMT+0200 (CEST)",
    "creator": {
      "id": "51fa1f5d-f295-4792-856b-6557a6ce07ce",
      "name": "Ruby Elliott"
    }
  },
  {
    "id": "43a024d0-e99e-48f1-9d4e-04d2ff961b6c",
    "picture": "http://placehold.it/128x128",
    "title": "consequat elit officia et laborum dolore",
    "createdAt": "Mon Sep 12 2016 07:37:26 GMT+0200 (CEST)",
    "creator": {
      "id": "cc2f7c36-a389-4a91-b04d-4d062f677ff1",
      "name": "Lindsey Kirk"
    }
  },
  {
    "id": "a6a337ae-da7d-4ed2-819e-b70ecb3f25a8",
    "picture": "http://placehold.it/128x128",
    "title": "est cupidatat consequat cillum sit commodo",
    "createdAt": "Tue Mar 28 2017 22:19:14 GMT+0200 (CEST)",
    "creator": {
      "id": "b6979a24-7113-4a08-9ff8-6dc0e4643a9e",
      "name": "Ila Lane"
    }
  },
  {
    "id": "f4340f85-0564-4210-b0b5-8eb5b227ae7f",
    "picture": "http://placehold.it/128x128",
    "title": "aliquip sit sit eu Lorem sunt",
    "createdAt": "Wed Oct 15 2014 09:33:26 GMT+0200 (CEST)",
    "creator": {
      "id": "4ccd96b3-93ba-4aa7-8424-1b70f6057c05",
      "name": "Mia Bird"
    }
  },
  {
    "id": "83dd19fa-90c0-4260-bb63-d7c9b4234373",
    "picture": "http://placehold.it/128x128",
    "title": "tempor cupidatat cupidatat dolor adipisicing id",
    "createdAt": "Sun May 22 2016 22:24:24 GMT+0200 (CEST)",
    "creator": {
      "id": "c427e106-a40b-4e3c-bd29-fd8b905366f8",
      "name": "Amparo Glass"
    }
  },
  {
    "id": "894cb4d1-a623-48d5-95f5-4db825bcd3d6",
    "picture": "http://placehold.it/128x128",
    "title": "incididunt et velit est mollit eiusmod",
    "createdAt": "Sun May 10 2015 20:52:32 GMT+0200 (CEST)",
    "creator": {
      "id": "5fc27bfb-dd78-4dff-a0c1-34f5f889fc9d",
      "name": "Veronica Hall"
    }
  },
  {
    "id": "381b2015-4e91-42a1-b655-f5e627160444",
    "picture": "http://placehold.it/128x128",
    "title": "et anim aute aliqua nulla mollit",
    "createdAt": "Sun Apr 17 2016 02:33:14 GMT+0200 (CEST)",
    "creator": {
      "id": "db0f72da-524a-467d-a6c3-fe51fa00a329",
      "name": "Angie Lynn"
    }
    "title": "do sunt irure ut pariatur dolor",
    "createdAt": "Mon Apr 27 2015 16:09:50 GMT+0200 (CEST)",
    "creator": {
      "id": "07b2ab4c-44e5-485c-83c0-d8b9e530266d",
      "name": "Eunice Hardy"
    }
  },
  {
    "id": "b451e57d-d16e-4e4d-836c-155a18c5134d",
    "picture": "http://placehold.it/128x128",
    "title": "aliqua qui esse ex dolore deserunt",
    "createdAt": "Sun May 24 2015 00:05:16 GMT+0200 (CEST)",
    "creator": {
      "id": "2464b6f3-9c57-4d09-b7e2-c0baa974ab53",
      "name": "Olson Pittman"
    }
  },
  {
    "id": "fb135f94-6427-4050-9e8a-511c12f4a42e",
    "picture": "http://placehold.it/128x128",
    "title": "dolore do adipisicing non culpa do",
    "createdAt": "Mon Feb 15 2016 09:24:33 GMT+0100 (CET)",
    "creator": {
      "id": "f62f7e6c-9695-41b2-b8cf-53372ddc6c80",
      "name": "Consuelo Molina"
    }
  },
  {
    "id": "293829f8-e6b0-4fc3-9f1b-0070105f3182",
    "picture": "http://placehold.it/128x128",
    "title": "culpa irure ex ea sit cillum",
    "createdAt": "Mon Jan 27 2014 09:46:37 GMT+0100 (CET)",
    "creator": {
      "id": "2db5b49a-5dff-4ad5-94db-bba32deb07d9",
      "name": "Woodward Deleon"
    }
  },
  {
    "id": "ef4ceb4e-afdb-42a0-8b97-35a20202c477",
    "picture": "http://placehold.it/128x128",
    "title": "ex sunt proident elit irure enim",
    "createdAt": "Mon Jan 16 2017 09:21:04 GMT+0100 (CET)",
    "creator": {
      "id": "a9d9aac7-b88e-4e91-8a88-25f63fab54f0",
      "name": "Dorothea Gould"
    }
  },
  {
    "id": "54e983b8-cad2-43a8-8464-50aa5f9cf397",
    "picture": "http://placehold.it/128x128",
    "title": "cillum consectetur dolore exercitation est fugiat",
    "createdAt": "Mon Mar 07 2016 01:47:38 GMT+0100 (CET)",
    "creator": {
      "id": "1e855321-35c2-4e2d-ad0b-c62d72412256",
      "name": "Elsie Bruce"
    }
  },
  {
    "id": "41409eea-9393-40b4-88c1-e95ea6c760b5",
    "picture": "http://placehold.it/128x128",
    "title": "duis officia eiusmod eiusmod excepteur reprehenderit",
    "createdAt": "Thu Apr 23 2015 17:23:27 GMT+0200 (CEST)",
    "creator": {
      "id": "a5c67a1e-06b2-4120-b592-e3c247601975",
      "name": "Juliette Goodman"
    }
  },
  {
    "id": "9304e424-4e84-4b8d-907e-2ebfa2f3f24f",
    "picture": "http://placehold.it/128x128",
    "title": "velit labore quis aliquip laboris id",
    "createdAt": "Sun Feb 23 2014 12:14:50 GMT+0100 (CET)",
    "creator": {
      "id": "f0774a6e-6f8b-4b28-916d-6b953f7e3015",
      "name": "Griffin Serrano"
    }
  },
  {
    "id": "c6ab1908-c24e-40ca-b6f7-9cbfbf9a2789",
    "picture": "http://placehold.it/128x128",
    "title": "occaecat incididunt irure nulla aliqua eu",
    "createdAt": "Fri Aug 07 2015 17:32:46 GMT+0200 (CEST)",
    "creator": {
      "id": "f20d8d89-b02f-41c3-b68f-e41a33c89b2a",
      "name": "England Figueroa"
    }
  },
  {
    "id": "3552918f-0317-4966-b439-5b954567c237",
    "picture": "http://placehold.it/128x128",
    "title": "occaecat aute pariatur ad anim esse",
    "createdAt": "Wed Jul 13 2016 14:00:03 GMT+0200 (CEST)",
    "creator": {
      "id": "0f0eb595-8344-48b4-99ae-4892db05e465",
      "name": "Bernice Marks"
    }
  },
  {
    "id": "216d93a6-7845-4e2d-9e0d-aa57125bff74",
    "picture": "http://placehold.it/128x128",
    "title": "sint non cillum excepteur in nulla",
    "createdAt": "Sat Jan 24 2015 10:34:23 GMT+0100 (CET)",
    "creator": {
      "id": "2d4530ed-232b-4b9f-b83f-928c51e63344",
      "name": "Bridget Kane"
    }
  },
  {
    "id": "2f233aee-18a7-4a1c-916c-0f888a5c3197",
    "picture": "http://placehold.it/128x128",
    "title": "ex mollit id reprehenderit fugiat ad",
    "createdAt": "Tue Nov 08 2016 21:59:29 GMT+0100 (CET)",
    "creator": {
      "id": "ca86ead5-3bd3-4f0c-9b26-356bd4ea6fb8",
      "name": "Rodriguez Cummings"
    }
  },
  {
    "id": "a0f80579-4319-40eb-a98c-1e147887cd2d",
    "picture": "http://placehold.it/128x128",
    "title": "velit id dolore labore pariatur voluptate",
    "createdAt": "Thu Dec 10 2015 03:31:11 GMT+0100 (CET)",
    "creator": {
      "id": "f1caeb66-d636-4aeb-b800-c16158a5e74e",
      "name": "Hodge Gentry"
    }
  },
  {
    "id": "f6aca6dc-7008-4257-9635-1adaa3229511",
    "picture": "http://placehold.it/128x128",
    "title": "nisi anim eu sunt aliqua in",
    "createdAt": "Fri Jun 10 2016 07:38:26 GMT+0200 (CEST)",
    "creator": {
      "id": "abedab4d-5c83-46fb-aff5-3e60961847d4",
      "name": "Dale Wolfe"
    }
  },
  {
    "id": "b704dfbe-9a50-4103-9b53-19b1a5e112a7",
    "picture": "http://placehold.it/128x128",
    "title": "do proident ex incididunt nisi qui",
    "createdAt": "Fri Mar 14 2014 18:05:35 GMT+0100 (CET)",
    "creator": {
      "id": "3c417b6b-5bcb-45a0-b71e-064d199ebe9d",
      "name": "Gardner Medina"
    }
  },
  {
    "id": "260cdc0b-0c81-4b60-8c6b-ce7523fd3094",
    "picture": "http://placehold.it/128x128",
    "title": "officia dolor fugiat exercitation nisi magna",
    "createdAt": "Thu Jan 16 2014 19:28:18 GMT+0100 (CET)",
    "creator": {
      "id": "5021198c-e5e0-4bf9-bbdf-ea59474e1cce",
      "name": "Lucy Mcgee"
    }
  },
  {
    "id": "a5da77cc-6ddc-4ec9-9507-ed6c015af035",
    "picture": "http://placehold.it/128x128",
    "title": "eu deserunt non ipsum esse velit",
    "createdAt": "Tue Sep 27 2016 07:50:20 GMT+0200 (CEST)",
    "creator": {
      "id": "d0d24573-1351-4d44-a724-6a98999f304b",
      "name": "Wilson Estes"
    }
  },
  {
    "id": "534cdebe-52df-44e2-a198-6efbf68ddccc",
    "picture": "http://placehold.it/128x128",
    "title": "ad ex excepteur non proident occaecat",
    "createdAt": "Tue Jun 23 2015 21:35:32 GMT+0200 (CEST)",
    "creator": {
      "id": "0555e75b-0d08-4b58-9e20-f652dd45d7a3",
      "name": "Hernandez Hodge"
    }
  },
  {
    "id": "073d3f4a-1ce7-4d24-873c-74605e434c54",
    "picture": "http://placehold.it/128x128",
    "title": "et pariatur laborum irure eu laboris",
    "createdAt": "Fri Jun 12 2015 01:20:42 GMT+0200 (CEST)",
    "creator": {
      "id": "52d12b55-73a2-45c4-8c29-4988b6255503",
      "name": "Walter Alvarez"
    }
  }

]


#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_task(/):
#    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
