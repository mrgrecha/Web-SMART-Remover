$("#tree")
	.bind("before.jstree", function (e, data) {
		// байндинг на событие перед загрузкой дерева
	})
	.jstree({
		// Подключаем плагины
		"plugins" : [
			"themes","json_data"
		],
		"json_data" : {
			"ajax" : {
				"url" : "tree.php", // получаем наш JSON
				"data" : function (n) {
					// необходиый коллбэк
				}
			}
		},
	})
	.bind("select_node.jstree", function(e, data){
		// байндинг на выделение нода
                // укажем ему открытие документа на основе якорей
                window.location.hash = "view_" + data.rslt.obj.attr("id").replace("node_","");
	})
});