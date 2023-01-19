import { useContext, useEffect, useState } from "react";
import Airtable from "airtable";

const base = new Airtable({apiKey: 'keyQ0V1l9vBkHkLev'}).base('appJQ2e3Bms1nlD3B');

var userRows = [];

var submissionRows = [];


export function Datatablesource() {
  

  useEffect(()=>{
    base("summary")
      .select({view: "Grid view"})
      .eachPage((records, fetchNextPage)=>{
        var rows = [];
        //console.log(records.length);
        for(var i in records){
          rows[i] ={
            "id": i+1,
            "problem": String(records[i].fields.title),
            "img": "https://user-images.githubusercontent.com/36547915/97088991-45da5d00-1652-11eb-900f-80d106540f4f.png",
            "difficulty": String(records[i].fields.difficulty),
            "status": String(records[i].fields.status),
            "submission times": String(records[i].fields.submission_times)
        }
 }
        userRows.push(rows);
        fetchNextPage();
      })
      base("submission_history")
      .select({view: "Grid view"})
      .eachPage((records, fetchNextPage)=>{
        var rows = [];
        //console.log(records);
        for(var i = 0; i< records.length; i++){
          rows[i] ={
            id : i+1,
            //key: String(records[i].fields.last_submission_status),
            last_submission_status: String(records[i].fields.last_submission_status),
            last_submission_time: String(records[i].fields.last_submission_time),
            
        }}
        submissionRows.push(rows);
        fetchNextPage();
      })
  }, []);

}
//console.log(userRows, submissionRows);

 
export const userColumns = [
  
  { field: "id", headerName: "ID", width: 70 },
  {
    field: "problem",
    headerName: "Problem",
    width: 330,
    renderCell: (params) => {
      return (
        <div className="cellWithImg">
          <img className="cellImg" src="https://user-images.githubusercontent.com/36547915/97088991-45da5d00-1652-11eb-900f-80d106540f4f.png" alt="avatar" />
          {params.row.problem}
        </div>
      );
    },
  },

  {
    field: "difficulty",
    headerName: "Difficulty",
    width: 100,
  },
  {
    field: "status",
    headerName: "Status",
    width: 100,
    renderCell: (params) => {
      return (
        <div className={`cellWithStatus ${params.row.status}`}>
          {params.row.status}
        </div>
      );
    },
  },
  {
    field: "submission times",
    headerName: "Sumission Times",
    width: 130,
  },
];

//test
//console.log(userRows);
//console.log(submissionRows);


export {userRows, submissionRows};
  
