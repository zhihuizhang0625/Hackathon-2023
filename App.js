import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import List from "./pages/list/List";
import Single from "./pages/single/Single";
import New from "./pages/new/New";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { productInputs, userInputs } from "./formSource";
import "./style/dark.scss";
import { useContext, useEffect, useState } from "react";
import { DarkModeContext } from "./context/darkModeContext";
import Airtable from "airtable";

const base = new Airtable({apiKey: 'keyQ0V1l9vBkHkLev'}).base('appJQ2e3Bms1nlD3B');



function App() {
  
  const [summary, setSummary] = useState([])
  const [submission_history, setSubmission_history] = useState([])

  useEffect(()=>{
    base("summary")
      .select({view: "Grid view"})
      .eachPage((records, fetchNextPage)=>{
        console.log(records);
        setSummary(records);
        fetchNextPage();
      })
      base("submission_history")
      .select({view: "Grid view"})
      .eachPage((records, fetchNextPage)=>{
        console.log(records);
        setSubmission_history(records);
        fetchNextPage();
      })
   

  }, []);
  const { darkMode } = useContext(DarkModeContext);

  return (
    <div className={darkMode ? "app dark" : "app"}>
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route index element={<Home />} />
            <Route path="login" element={<Login />} />
            <Route path="users">
              <Route index element={<List />} />
              <Route path=":userId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={userInputs} title="Add New User" />}
              />
            </Route>
            <Route path="products">
              <Route index element={<List />} />
              <Route path=":productId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={productInputs} title="Add New Product" />}
              />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
