# PenIt-Personal Blogging Website
 Project made using Django and sqlite inbuild. Recieved text input from summernote and images from unsplash. 
 
 Users who are very fond of writing blogs and always wanted a blog of their own can have it and utilise it for changing their hobby into a passion.
 
 
 
 # How to run project after downloading?
 1. Enter folder "try Django" where manage.py is present using your cmd or linux terminal.
 2. Make sure that django, django-summernote and pillow is installed in your environment or system.
 3. If the above modules are not installed then type "pip install module_name" in you terminal. (Eg. pip install django-summernote)
 4. Type "python manage.py runserver" in cmd.
 5. Voila!!! your server is running on your local machine. 
 6. Just go to the link displayed in the cmd through your favourite browser.
 7. You will see website running.
 8. If you want to login then credentials is 
         Username: joshi ,
         Password: hello123 .
    This is not my personal password so don't try. xD
 9. If you want to change password then write "python manage.py createsuperuser" in cmd opened in first step.
 
 
 # What it could do?
 1. Help you create blogs and display it in the webpage... Not just it and many more.
 2. You can totally manage how your blogs will look like using summernote.
 3. Blogs are accompanied by display picture that describes your blog. This is not compulsory.
 4. Then you can create slug for your webpage links. Like www.penit.com/blog/dog_is_best  <= here Slug is dog_is_best
 5. You can decide to publish it in your website or make it a draft by either giving publish date or not respectively.
 6. Latest blogs will be displayed in the main page.
 7. And blog page will display every blog. It will display your drafts only if you are logged in. So readers will see only your published items.
 8. You can update an existing blog.
 9. Search for your blogs through search button at the top. And it not only search from titles of your blog but also contents of your blog.
 10. Only you can create a blog, edit it and delete it.


 # Now if you want it, you can use it.
 I would be glad if you mention last line in your website but that's fine with me if you do not. So to summerize that it is open to be used by anyone and everyone out there.
 
 I have now successfully launched it on heroku[https://penit-blog.herokuapp.com/] though since heroku server sleeps and static data is lost after some time, so need to have good server.  But for demo you could hop here[https://penit-blog.herokuapp.com/] . 
