module(unparameterized("MoBL-Data"),[imports([module(unparameterized("Common")),module(unparameterized("MoBL"))])],[exports(conc-grammars(context-free-syntax([prod([iter-star(sort("MetaAnno")),lit("\"entity\""),sort("QId"),lit("\":\""),sort("Type"),lit("\"{\""),iter-star(sort("EntityBodyDecl")),lit("\"}\"")],sort("Definition"),attrs([term(default(appl(unquoted("cons"),[fun(quoted("\"Entity\""))])))])),prod([iter-star(sort("MetaAnno")),lit("\"entity\""),sort("QId"),lit("\"{\""),iter-star(sort("EntityBodyDecl")),lit("\"}\"")],sort("Definition"),attrs([term(default(appl(unquoted("cons"),[fun(quoted("\"EntityNoSuper\""))])))])),prod([iter-star(sort("MetaAnno")),sort("ID"),lit("\":\""),sort("Type"),lit("\"(\""),iter-star-sep(sort("Anno"),lit("\",\"")),lit("\")\"")],sort("EntityBodyDecl"),attrs([term(default(appl(unquoted("cons"),[fun(quoted("\"Property\""))])))])),prod([iter-star(sort("MetaAnno")),sort("ID"),lit("\":\""),sort("Type")],sort("EntityBodyDecl"),attrs([term(default(appl(unquoted("cons"),[fun(quoted("\"PropertyNoAnnos\""))])))])),prod([sort("FunctionDef")],sort("EntityBodyDecl"),no-attrs),prod([sort("ID")],sort("Anno"),attrs([term(default(appl(unquoted("cons"),[fun(quoted("\"SimpleAnno\""))])))])),prod([lit("\"inverse\""),lit("\":\""),sort("ID")],sort("Anno"),attrs([term(default(appl(unquoted("cons"),[fun(quoted("\"InverseAnno\""))])))]))]),context-free-syntax([prod([lit("\"@sync\""),sort("UriPath")],sort("MetaAnno"),attrs([term(default(appl(unquoted("cons"),[fun(quoted("\"SyncEntityAnno\""))])))]))])))])