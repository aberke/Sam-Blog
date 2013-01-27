from django.contrib import admin
from main_site.models import Post, Header


class Header_Admin(admin.ModelAdmin):
	fieldsets = [
		('Your Main Heading Text', {'fields':['heading',],
				'description': 'This is the text that will show up in your header',
			}),
		('Background Image', {'fields':['background_image_url',],
				'description': 'Select your image on your imgur account and use the "generate link" option.  Choose to generate a <strong>direct</strong> link.  For example your input to this field should look something like "http://i.imgur.com/X8Uaz.jpg".  Maybe someday when I want to be more fancy Ill use the imgur api to automate this for you.  Also to note:  Try to make this image as small in size as possible (in terms of KB) so that it doesnt take a while to load on the page when stretched out across the top.'
			}),
		('Title Tab', {'fields':['title_image_url','title_text',],
				'description': 'This is the image and text that youll see in the tabbed bar at the top of the browser.  If you dont put an image here Ill just insert the same image as the background image.  Same imgur instructions as above.  If you dont put title text here, itll just be blank and your site will be mad mysterious....',
			}),
	]
admin.site.register(Header, Header_Admin)


class Post_Admin(admin.ModelAdmin):
	list_display = ('title', 'date_posted')
	fieldsets = [
		('Title and Date', {'fields': ['title','date_posted',],
				'description': 'I know you dont want a Title and Date-Posted to be shown, but I want you to have some way to sort through your own photos and I want to use the date to order the photos.  The title is what youll see when youre editing your site.  Im also using the title in the (unseen unless looking at html source code) "title" field for the photo.  This means its what webcrawlers will see.  So if for example you title it "Chicos favorite", someone who searches google images with "Chicos favorite" will probably see your photo.  If this concept bothers you, then let me know, Im just doint it because I figured youd enjoy some extra page hits.',
			}),
		('The photoooo', {'fields': ['image_url',],
				'description': 'Same instructions as with the header: Select your image on your imgur account and use the "generate link" option.  Choose to generate a <strong>direct</strong> link.  For example your input to this field should look something like "http://i.imgur.com/X8Uaz.jpg".  Maybe someday when I want to be more fancy Ill use the imgur api to automate this for you.',
			}),
		('Optional "Story/Header"', {'fields': ['story_header', 'story_text',],
				'description': 'You can leave either one of these, or both blank, but heres how Im going to handle it:  If you provide just a "Story/Header" then thats all people will see under the photo and it wont be a collapsible.  If you provide just a "story text" then the default header for that text will be "Story" so that the user will know to expand it.  If you want it blank just put a space there, but it might look stupid because itll be a blank blob.',
				'classes': ['collapse'],
				}),
	]
admin.site.register(Post, Post_Admin)
