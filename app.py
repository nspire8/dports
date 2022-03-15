import re

from bottle import route, run, template

# shamelessly stolen from https://www.w3schools.com/howto/howto_js_sort_table.asp
js = """
<script>
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("tbl");
  switching = true;
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n].innerHTML.toLowerCase();
      y = rows[i + 1].getElementsByTagName("TD")[n].innerHTML.toLowerCase();
      if (y.includes("-&gt;")) {
          xNum = x.match( /\d+/ )
          x = Number(xNum[0]);
          yNum = y.match( /\d+/ )
          y = Number(yNum[0]);
      }
      if (dir == "asc") {
        if (x > y) {
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x < y) {
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
</script>
"""

css = """
<style>
    table {
        border-collapse: collapse;
    }
    th {
        text-align: left;
    }
    th:hover {
        cursor: pointer;
    }
    table, th, td {
        border: 1px solid;
    }
    th, td {
        padding-left: 10px;
        padding-right: 10px;
        padding-top: 5px;
    }
    tr:hover {
        background-color: coral;
    }
</style>
"""

head = f"<head>{js}{css}</head>"

@route("/")
def index():
    html = f"<html>{head}<body><table id=\"tbl\"><tr><th onclick=\"sortTable(0)\">Ports</th><th onclick=\"sortTable(1)\">Container Name</th></tr>"
    output = []
    with open('/code/ports.txt') as f:
        raw = f.readlines()
        for l in raw:
            words = [w.strip(',').lstrip('0.0.0.0:') for w in l.split() if ":::" not in w]
            container = words[-1]
            ports = [w for w in words[:-1] if "->" in w]
            for port in ports:
                row = f"<tr><td>{port}</td><td>{container}</td></tr>"
                output.append(row)

    key = lambda s: int(re.search(r'\d+', s)[0])
      
    html += "".join(sorted(output, key=key)) + "</table></body></html>"
    return html

run(host='0.0.0.0', port=80, debug=True)
