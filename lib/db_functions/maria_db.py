from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "jdbc:mariadb://localhost:3306/"

db = SQLAlchemy(app)

def match_dict_key(key,dictionary):
   if dictionary[key]:
      return True
   return False

def match_dict_keys(key,list_of_dictionaries):
   length_of_dictionary_list = len(list_of_dictionaries)
   key_list =[key]*length_of_dictionary_list
   result = filter(match_dict_key,zip(key_list,list_of_dictionaries))
   result = set(list(result))
   return result


def add_customer(customer_id, customer_name):
  image_collection.insert_one({'customer_id':customer_id})
  user_data_collection.insert_one({'customer_id':customer_id, "customer_name": customer_name})
  playlist_collection.insert_one({'customer_id':customer_id})
  screen_collection.insert_one({'customer_id':customer_id})

def delete_customer(customer_id):
  image_collection.delete_one({'customer_id':customer_id})
  user_data_collection.delete_one({'customer_id':customer_id})
  playlist_collection.delete_one({'customer_id':customer_id})
  screen_collection.delete_one({'customer_id':customer_id})


#MOVED TO THE HANDLER
# 'playlists' : [{'playlist1_name': ['image1_name', 'image2_name']}, {'playlist2_name': ['image3_name', 'image4_name']}]
# def add_playlist(customer_id,playlist_name, description):
#       customer_entry = playlist_collection.find_one({'customer_id':customer_id})                                                    
#       print (customer_entry)
#       playlist_exists = False
#       #check if playlists exists already
#       if 'playlists' in customer_entry:
#             for playlist_dict in customer_entry['playlists']:
#                  if playlist_name in playlist_dict:
#                       playlist_exists = True
#       if playlist_exists:
#             return {'status':'success', 'message':'Playlist already exists!'}, 200
#       else:
#             dct = {playlist_name: [], 'description': description}
#             playlist_collection.update_one({"customer_id": customer_id}, { "$push": { "playlists":dct}})
#             return {'status':'success', 'message':'Playlist created successfully!'},200

#MOVED TO THE HANDLER
# def remove_playlist(customer_id, playlist_name):
#       customer_entry = playlist_collection.find_one({'customer_id':customer_id})                                                    
#       print (customer_entry)
#       playlists = customer_entry['playlists']
#       playlist_content = list(filter(lambda dct: dct if(playlist_name in dct) else None, playlists))[0]
#       print ("playlist_content :",playlist_content)
#       playlist_collection.update_one({"customer_id": customer_id}, { "$pull": { "playlists": playlist_content }})
#       return {'status':'success', 'message':'Playlist deleted successfully!'}, 200


# MOVED TO HANDLER 
# def add_to_playlist(customer_id, playlist_name, content, image_duration):
#       customer_entry = playlist_collection.find_one({'customer_id': customer_id})                                                    
#       print(customer_entry)
#       playlists = customer_entry['playlists']
#       playlist_content = list(filter(lambda dct: dct if(playlist_name in dct) else None, playlists))[0]
#       print(playlist_content)
#       playlist_collection.update_one({"customer_id": customer_id}, { "$pull": { "playlists": playlist_content }})
#       new_list = playlist_content[playlist_name]
#       new_list.extend(content)
#       playlist_collection.update_one({"customer_id": customer_id}, { "$push": { "playlists": {playlist_name: new_list, 'description': playlist_content['description']} } } )
#       # ADD LOGIC TO CREATE AND SAVE THE PLAYLIST IN THE FILESYSTEM
#       playlist_content_path = f'/{customer_id}/images/'
#       playlist_path = f'/{customer_id}/playlists/'
#       images_file_list = [os.path.join(playlist_content_path, image_file) for image_file in new_list]
#       clips = [ImageClip(image).set_duration(image_duration) for image in images_file_list]
#       concat_clip = concatenate_videoclips(clips, method="compose")
#       playlist_file_path = os.path.join(playlist_path, f"{playlist_name}.mp4")
#       if not os.path.exists(playlist_file_path):
#            print ("creating playlist file now")
#            print (f"{playlist_file_path=}")
#            print (f"{playlist_name=}")
#            open(playlist_file_path,'w').close()
#            print ("playlist file created")
#       concat_clip.write_videofile(os.path.join(playlist_path, f"{playlist_name}.mp4") , threads = 8, fps=24)
#       return {'status':'success', 'message':'Image added successfully to the playlist!'}, 200


#MOVED TO THE HANDLER
# def remove_from_playlist(customer_id, playlist_name, content):
#       customer_entry = playlist_collection.find_one({'customer_id': customer_id})                                                    
#       print(customer_entry)
#       playlists = customer_entry['playlists']
#       playlist_content = list(filter(lambda dct: dct if(playlist_name in dct) else None, playlists))[0]
#       playlist_collection.update_one({"customer_id": customer_id}, { "$pull": { "playlists": playlist_content }})
#       orig_list = playlist_content[playlist_name]
#       new_list = list(filter(lambda i: i not in content, orig_list))
#       playlist_collection.update_one({"customer_id": customer_id}, { "$push": { "playlists": {playlist_name: new_list} }})
#       return {'status':'success', 'message':'Image deleted successfully from the playlist!'}, 200


#MOVED TO THE HANDLER
# def list_playlists(customer_id):
#       customer_entry = playlist_collection.find_one({'customer_id': customer_id})                                                    
#       print(customer_entry)
#       playlists = customer_entry['playlists']
#       playlist_names = []
#       for playlist in playlists:
#            playlist_name = list(playlist.keys())[0]
#            playlist_names.append(playlist_name)
#       print(playlist_names)
#       return {'status':'success', 'message':'Playlists are listed successfully!', 'playlists': playlist_names}, 200


#MOVED TO THE HANDLER
# def list_images_from_playlist(customer_id, playlist_name):
#       customer_entry = playlist_collection.find_one({'customer_id': customer_id})                                                  
#       print(customer_entry)
#       playlists = customer_entry['playlists']
#       print(playlists)
#       # images = list(filter(lambda dct: dct if(playlist_name in dct) else None, playlists))[0][playlist_name]
#       images = list(filter(lambda dct: dct if(playlist_name in dct) else None, playlists))[0]
#       print(images)
#       number_of_content = len(images[playlist_name])
#       return {'status':'success', 'number_of_content': number_of_content, 'total_runtime': (number_of_content*30), 'message':"Playlist's contents are listed successfully", 'playlist_content': images}, 200

# MOVED TO HANDLER
# def list_images(customer_id):
#       customer_entry = image_collection.find_one({'customer_id': customer_id})                                                 
#       print(customer_entry)
#       images_list = customer_entry['images_list']
#       for image in images_list:
#            for key in image:
#                image[key] = image[key].decode('utf-8')
#       print(images_list)
#       return {'status':'success', 'message':'Images are listed successfully for the customer!', 'images_list': images_list}, 200


def customer_image_deletion(customer_id, content):
      customer_entry = image_collection.find_one({'customer_id': customer_id})
      playlists = playlist_collection.find_one({'customer_id': customer_id})['playlists']    
      # playlists = [{'playlistName': ['image1Name', 'image2Name']}, {'playlistName': ['image1Name', 'image2Name']}, {'playlistName': ['image1Name', 'image2Name']}s]                                     
      print(customer_entry)
      images_list = customer_entry['images_list']
      #DELETE FROM IMAGE COLLECTION AND PLAYLIST COLLECTION
      #NEED TO IMPROVE THE COMPLEXITY AND NOT GO WITH BRUTE FORCE
      #DELETING IMAGES FROM THE IMAGE COLLECTION
      new_images_list = list(filter(lambda image: image.keys() not in content, images_list))
      image_collection.update_one( {"customer_id": customer_id}, { "$set": { "images_list": new_images_list } } )
      for playlist_name, playlist_images_list in playlists.items():
         #   playlist = {'playlistName': ['image1Name', 'image2Name']}
         for image in content:
              if image in playlist_images_list:
                 playlist_images_list.remove(image)
         playlist_collection.update_one( {"customer_id": customer_id}, { "$pull": { "playlists": {playlist_name: playlist_images_list} }})
                



      # if isinstance(content, list):
      #      for image in content:
      #           for playlist in playlists:
      #                if image in list(playlist.values()):
      #                   return {'status':'fail','message':'Images deletion failed for the customer as it is being used in the playlist/s'}
                
                          
                

      image_collection.update_one({"customer_id": customer_id}, { "$push": { "images_list": images_list}})


# MOVED TO HANDLER
# def add_screen(customer_id, screen_name, description):
#       customer_entry = screen_collection.find_one({'customer_id':customer_id})                                                    
#       print (customer_entry)
#       #check if screen exists already
#       if ('screens' in customer_entry) and (screen_name in customer_entry['screens']):
#             return {'status':'success', 'message':'Screen already exists!'},200
#       else:
#             dct = {screen_name: [], 'description': description}
#             screen_collection.update_one({"customer_id": customer_id}, { "$push": { "screens":dct}})
#             return {'status':'success', 'message':'Screen added successfully!'},200


# MOVED TO HANDLER
# def list_screens(customer_id):
#       customer_entry = screen_collection.find_one({'customer_id': customer_id})
#       print(customer_entry)
#       screens = customer_entry['screens']
#       screen_names = []
#       for screen in screens:
#            screen_name = list(screen.keys())[0]
#            screen_names.append(screen_name)
#       print(screen_names)
#       return {'status':'success', 'message':'Screens are listed successfully!', 'screens': screen_names}, 200


# MOVED TO HANDLER
# def remove_screen(customer_id, screen_name):
#       customer_entry = screen_collection.find_one({'customer_id':customer_id})                                                    
#       print (customer_entry)
#       screens = customer_entry['screens']
#       screen_content = list(filter(lambda dct: dct if(screen_name in dct) else None, screens))[0]
#       print ("screen_content :",screen_content)
#       screen_collection.update_one({"customer_id": customer_id}, { "$pull": { "screens": screen_content }})
#       return {'status':'success', 'message':'Playlist deleted successfully!'},200


# 'screens' : [{'screen1_name': ['playlist1_name', 'playlist2_name'], 'description': 'abcd'}, {'screen2_name': ['playlist3_name', 'playlist4_name']}]
# MOVED TO HANDLER
# def list_playlists_from_screen(customer_id, screen_name):
#       customer_entry = screen_collection.find_one({'customer_id': customer_id})                                                  
#       print(customer_entry)
#       screens = customer_entry['screens']
#       playlists = list(filter(lambda dct: dct if(screen_name in dct) else None, screens))[0]
#       number_of_content = len(playlists[screen_name])
#       return {'status':'success', 'number_of_content': number_of_content, 'total_runtime': (number_of_content*30), 'message': "Screen's content are listed successfully", 'screen_content': playlists}, 200