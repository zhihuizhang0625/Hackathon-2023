import "./table.scss";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

const List = () => {
  const rows = [
    {
      id: 1143155,
      status: "Approved",
      date: "1 March"
    },
    {
      id: 2235235,
      date: "1 March",
      status: "Pending"
    },
    {
      id: 2342353,
      status: "Pending",
      date: "1 March"
    },
    {
      id: 2357741,
      status: "Approved",
      date: "31 March",
    },
    {
      id: 2342355,
      status: "Pending",
      date: "1 March"
    },
  ];
  return (
    <TableContainer component={Paper} className="table">
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell className="tableCell">Submission ID</TableCell>
            <TableCell className="tableCell">Status</TableCell>
            <TableCell className="tableCell">Date</TableCell>
 
            
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell className="tableCell">{row.id}</TableCell>

              <TableCell className="tableCell">
                <span className={`status ${row.status}`}>{row.status}</span>
              </TableCell>
              <TableCell className="tableCell">{row.date}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default List;
