
const Navbar =()=>{
    return (
        <nav className= " p-4 my-2 mx-2  " >
        <div className="container mx-auto flex justify-between items-center w-4/5 my-2  " >
          <div className ="flex justify-between" >
          <h1 className=" text-2xl font-bold mr-4" > Xmentor < /h1>
            < ul className = "flex space-x-4 m-6 " >
              <li>Mentors < /li>
              < li > Questions < /li>
              < li > Ressources < /li>
              < li > Job < /li>
              < li > A Propos < /li>
                < /ul>
                < /div>
                < ul className = "flex space-x-4 " >
                  <li>Login < /li>
                  < li > Signup < /li>
                  < /ul>
                  < /div>
                  < /nav>
      );
}

export default Navbar