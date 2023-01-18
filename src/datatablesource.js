export const userColumns = [
  { field: "id", headerName: "ID", width: 70 },
  {
    field: "problem",
    headerName: "Problem",
    width: 330,
    renderCell: (params) => {
      return (
        <div className="cellWithImg">
          <img className="cellImg" src={params.row.img} alt="avatar" />
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

//temporary data
export const userRows = [
  {
    "id": 1,
    "problem": "53. Maximum Subarray",
    "img": "https://user-images.githubusercontent.com/36547915/97088991-45da5d00-1652-11eb-900f-80d106540f4f.png",
    "difficulty": "Medium",
    "status": "Solved",
    "submission times": "2"
},{
    "id": 2,
    "problem": "55. Jump Game",
    "img": "https://user-images.githubusercontent.com/36547915/97088991-45da5d00-1652-11eb-900f-80d106540f4f.png",
    "difficulty": "Medium",
    "status": "Attempted",
    "submission times": "3"
},{
    "id": 3,
    "problem": "232. Implement Queue using Stacks",
    "img": "https://user-images.githubusercontent.com/36547915/97088991-45da5d00-1652-11eb-900f-80d106540f4f.png",
    "difficulty": "Easy",
    "status": "Attempted",
    "submission times": "1"
},
];
