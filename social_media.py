from gluon.tools import Service
service = Service()

def crud_menu():
#    response.flash = T("Hello World")  
    response_dict={
        "message":"Ths is Menu for CRUD"
    }
    return response_dict

def create_post():
#    response.flash = T("Hello World")   
    if request.vars.post_submit:
        # response.flash="I got you"
        response.flash=request.vars.image_post
        db.post_data.insert(user_name=request.vars.user_name,heading=request.vars.post_title,body=request.vars.post_body)
        # http://127.0.0.1:8000/learning1/social_media/api/create/sahil/1/this%20is%20my%20house
    response_dict={
        "message":"This is place for creating posts"
    }
    return response_dict

def view_post():   
    rows_data=db().select(db.post_data.ALL)
    response.view="social_media/create_post.html"
    response_dict={
        "rows_data":rows_data
    }
    return response_dict

# def call():
#     session.forget()
#     return service()

# @service.run
# def concat(a, b):
#     return a + b


@request.restful()
def api():

    def GET(*args, **vars):
        user_name=args[0]
        return_data=db(db.post_data.user_name==user_name).select()
        if any(return_data)==False:
            raise HTTP(404,"No data Found")
        return dict(return_data=return_data)

    def POST(*args, **vars):
        user_name=args[0]
        heading=args[1]
        body=args[2]
        try:
            db.post_data.insert(user_name=user_name,heading=heading,body=body)
        except:
            raise HTTP(400,"Unsuccessfull Request")
        raise HTTP(201,"Successfull Request")

    def PUT(*args, **vars):
        user_name=args[0]
        heading=args[1]
        updated_body=args[2]
        cnt=db(db.post_data.user_name == user_name, db.post_data.heading==heading).update(body=updated_body)
        print(cnt,user_name,"----")
        if cnt>0:
            raise HTTP(200,"Successfull Request")
        else:
            raise HTTP(204,"No record Found")

    def DELETE(*args, **vars):
        user_name=args[0]
        heading=args[1]
        cnt=db(db.post_data.user_name == user_name, db.post_data.heading==heading).delete()
        if cnt>0:
            raise HTTP(200,"Successfull Request")
        else:
            raise HTTP(204,"No record Found")

    return locals()