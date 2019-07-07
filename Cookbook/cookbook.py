from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/recipe_new')
def recipe_new():
    conn = sql.connect('cookbook.db3')
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute('SELECT * FROM Category ORDER BY Category ASC')
    cat_rows = cur.fetchall()

    cur2 = conn.cursor()
    cur2.execute('SELECT Ingredient FROM Ingredients ORDER BY Ingredient ASC')
    ings_rows = cur2.fetchall()
    conn.close()
    return render_template('recipe_new.html', rows=cat_rows, ings=ings_rows)


@app.route('/category_new')
def add_category():
    conn = sql.connect('cookbook.db3')
    new_category = request.args.get('new_category')
    cur = conn.cursor()
    cur.execute("INSERT INTO Category (Category) VALUES ('" + new_category + "')")
    conn.commit()
    conn.close()
    return ('', 204)

@app.route('/ingredient_new')
def add_ingredient():
    conn = sql.connect('cookbook.db3')
    new_ingredient = request.args.get('new_ingredient')
    new_ing_unit = request.args.get('new_ing_unit')

    cur = conn.cursor()
    cur.execute("INSERT INTO Ingredients (Ingredient, Measure_Unit) VALUES ('" + new_ingredient + "', '" + new_ing_unit + "')")
    conn.commit()
    conn.close()
    return ('', 204)

@app.route('/recipe_add')
def add_recipe():
    if request.method == 'POST':
        try:
                    recipe_name = request.form['recipe_name']
                    category = request.form['category']
                    servings = request.form['servings']
                    prep_time = request.form['prep_time']
                    cook_time = request.form['cook_time']

                    ing = []
                    ing_count = []

                    for i in range(request.form['num_of_ing']):
                        if ("ing"+(str(i))) in request.form:
                            ing.append(request.form['ing'+str(i)])
                            ing_count.append(request.form['ing_count'+str(i)])

                    conn = sql.connect('cookbook.db3')




if __name__ == '__main__':
    app.run(debug=True)