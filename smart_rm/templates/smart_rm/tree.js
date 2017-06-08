// The fs on the require('fs') is a library to deal with files/folders
var fs = require('fs');

// path is used just to get delimiter, which is '/' on Linux and '\' on Windows.'
var path = require('path');

// Utils is here just to output on the console. Can be safely removed if/when the last console.log line is replaced by real functionality.
var util = require('util');


// EXAMPLE OF IMPLEMENTATION USING CALLBACKS.
//
// NOT FULLY IMPLEMENTED BUT KEPT FOR STUDYING PURPOSES.
// WOULD REQUIRE WORKING AROUND ASYNC TO BUILD JSON PROPERLY.
//
// var dir = function (path) {
//   fs.readdir(path, function (err, files) {
//     if (err) {
//       console.log(err);
//     } else {
//      files.forEach(function(file) {
//       var newPath = path + '/' + file;
//       fs.stat(newPath, function(err, stats) {
//         if (err) {
//           console.log(err);
//         } else {
//           if (stats.isDirectory()) {
//             dir(newPath); // Possibly array.push(dir(newPath)) or obj[newPath] = dir(newPath) ...?
//           }
//         }
//       });
//     });
//     }
//   });
// }


var id = 1;

var dir = function (basePath, parent) {
  var jsonTree = [];
  var items;

  try {
    items = fs.readdirSync(basePath);
  } catch (e) {
    return null;
  }

  for (var itemCounter=0; itemCounter < items.length; itemCounter++) {
    var itemName = items[itemCounter];
    var newPath = basePath + path.sep + itemName;
    var stats;

    try {
      stats = fs.statSync(newPath);
    } catch (e) {
      return null;
    }

    var item = {
      id: id++,
      text: itemName
    };

    if (parent != null) {
      item.parent = parent
    }

    if (stats.isDirectory()) {
      var children = dir(newPath, item.id);
      if (children != []) {
        item.children = children; // Possibly array.push(dirSync()) or obj[newPath] = dirSync() ...?
      }

      // IF YOU DON'T WANT TO LISTEN FILES, JUST THE FOLDERS, MOVE ~jsonTree.push(item);~ to here, inside this "if"
    }

    jsonTree.push(item);
  }

  return jsonTree;
}

// Replace "C:\SOME_FOLDER" with the path you want to build the tree for. This is the function to build the tree.
//
// WARNING: WILL GO AS DEEP AS NEEDED AND MAY TAKE A LONG TIME TO FINISH. CHOOSE A PATH WITH FEW ITEMS IN THE TREE.
//
var jsonStructure = dir('/Users/Dima', null);

// Saving the JSON to a file
// Careful. The file could be saved at weird locations depending on how you run the program.
//
// FS docs are not very clear on how it works, and/or if providing a full path such as "C:\folderTree.json" would work.
// You also need permissions to create a file at the directory for it to work.
//
var fileName = 'folderTree.json';
fs.writeFile(fileName, jsonStructure, function (err) {
  if (err) throw err;
  console.log('File saved to '+fileName+'!');
});

// JUST TO OUTPUT THE JSON.
// utils.inspect ENSURES ALL SUBFOLDERS AND FILES APPEAR ON console.log
// Can be easily remved,
console.log(util.inspect(jsonStructure, false, null));