import "./Failedlist.scss"
import Sidebar from "../../components/sidebar/Sidebar"
import Navbar from "../../components/navbar/Navbar"
import Failedtable from "../../components/Failedtable/Failedtable"

const FailedList = () => {
  return (
    <div className="Failedlist">
      <Sidebar/>
      <div className="FailedlistContainer">
        <Navbar/>
        <Failedtable/>
      </div>
    </div>
  )
}

export default FailedList