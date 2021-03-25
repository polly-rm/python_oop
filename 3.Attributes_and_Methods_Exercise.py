# 1.Photo Album
# class PhotoAlbum:
#     def __init__(self, pages):
#         self.pages = pages
#         self.photos = [[] for _ in range(self.pages)]
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         return cls(pages=photos_count // 4)
#
#     def add_photo(self, label: str):
#         for page in self.photos:
#             if len(page) < 4:
#                 page.append(label)
#                 return f"{label} photo added successfully on page {self.photos.index(page)+1} slot {page.index(label)+1}"
#         return "No more free spots"
#
#     def display(self):
#         result = "-----------\n"
#         for page_i in range(len(self.photos)):
#             for photo_slot_i in range(len(self.photos[page_i])):
#                 if self.photos[page_i][photo_slot_i]:
#                     self.photos[page_i][photo_slot_i] = "[]"
#             result += f"{' '.join(self.photos[page_i])}\n"
#             result += "-----------\n"
#         return result






