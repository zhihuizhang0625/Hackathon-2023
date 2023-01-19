import "./Reviewlist.scss"
import Sidebar from "../../components/sidebar/Sidebar"
import Navbar from "../../components/navbar/Navbar"
import Reviewtable from "../../components/Reviewtable/Reviewtable"

const ReviewList = () => {
  return (
    <div className="Reviewlist">
      <Sidebar/>
      <div className="ReviewlistContainer">
        <Navbar/>
        <Reviewtable/>
      </div>
    </div>
  )
}

export default ReviewList