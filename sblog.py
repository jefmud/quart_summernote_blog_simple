from quart import (abort, Quart, redirect, render_template, request, url_for)
from tinymongo import TinyMongoClient
    
app = Quart(__name__)
DB = TinyMongoClient().blog

@app.errorhandler(404)
async def page_not_found(e):
    """404 error handler-- 404 status set explicitly"""
    return await render_template('404.html'), 404
            
@app.route('/')
async def index():
    """return all the pages to a user view"""
    pages = DB.blog.find()
    return await render_template('page_list.html', pages=pages)

@app.route('/view/<id>')
async def page_view(id):
    """view a page by id or 404 if does not exist"""
    page = DB.blog.find_one({'_id':id})
    if page is None:
        # 
        abort(404)
    
    return await render_template('view.html', page=page)


@app.route('/edit', methods=['GET','POST'])
@app.route('/edit/<id>', methods=['GET','POST'])
async def page_edit(id=None):
    """edit serves to edit an existing page with a particular id, or create a new page"""
    status = ''
    if id:
        # find the page by its id, if it doesn't exist page = None, abort to 404 page
        page = DB.blog.find_one({'_id':id})
        if page is None:
            abort(404)
    else:
        # new page starts as a blank document
        status = 'Creating a new page.'
        page = {'title': '', 'content': ''}
    
    if request.method == 'POST':
        # check if user cancel was pressed.
        if (await request.form)['submit'] == 'cancel':
            if id:
                # user canceled a page edit, return to page view
                return redirect(url_for('page_view', id=id))
            else:
                # user canceled a new page creation, return to index
                return redirect(url_for('index'))
            
        # user hit submit, so get the data from the form.
        page['title'] = (await request.form).get('title')
        page['content'] = (await request.form).get('editordata')
        # look for required title and content
        if page['title'] != '' and page['content'] != '':
            # now, update or insert into database
            if id:
                # update an existing page
                DB.blog.update_one({'_id':id}, page)
            else:
                # insert a new page and get its id.
                id = DB.blog.insert_one(page).inserted_id
            # redirect to page view
            return redirect(url_for('page_view', id=id))
        else:
            # indicate a failure to enter required data
            status = 'ERROR: page title and content are required!'
        
    return await render_template('edit.html', page=page, status=status)

@app.route('/delete/<id>')
async def page_delete(id):
    """delete a page of a particular id, and return to top-level index"""
    page = DB.blog.find_one({'_id':id})
    if page is None:
        abort(404)
    
    DB.blog.delete_one({'_id':id})
    return redirect(url_for('index'))

if __name__ == '__main__':
    # note: app.run should not be used in production for a variety of reasons.
    app.run(debug=False, port=5000, host='0.0.0.0')
