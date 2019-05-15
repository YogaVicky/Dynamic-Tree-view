@app.route("/shot", methods=['GET', 'POST'])
def shot():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        userLogin = session.get('username')
        sql = "select proj_id,thumbnail,scope_category_id,scope_name,scope_description,SAP,production_status,scope_id from scope where proj_id=70"
        proj_list = get_lcl(sql)
        proj_dict = []
        for j in proj_list:
            k = dict(proj_id=j[0], thumnail=j[1], category=j[2], name=j[3], description=j[4], SAP=j[5], status=j[6], scope_id=j[7])
            proj_dict.append(k)
        sql2 = "SELECT scope_id,task_type_name,assigned_to,EMD,CMD,task_status,latest_int_version,latest_client_version,bid_end FROM `task` WHERE proj_id=70 "
        task_list = get_lcl(sql2)
        task_dict = []
        for j in task_list:
            k = dict(scope_id=j[0], task=j[1], assigned=j[2], emd=j[3], cmd=j[4], status=j[5], intversion=j[6], clientversion=j[7], due=j[8])
            task_dict.append(k)
        l = len(task_dict)
        sql3 = "SELECT category_id,category_name,super_category FROM `scope_category` WHERE projid=70 "
        scope_list = get_lcl(sql3)
        scope_dict = []
        for j in scope_list:
            k = dict(c_id=j[0], c_name=j[1], sc_id=j[2])
            scope_dict.append(k)
        return render_template ("shot.html", proj_dict=proj_dict, task_dict=task_dict, scope_dict=scope_dict,l=l)
