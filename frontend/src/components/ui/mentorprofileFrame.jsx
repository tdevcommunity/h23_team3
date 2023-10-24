
const MentorProfileFrame = ({ name, profession, stars, image }) => {
  return (
    <div className="border h-80 w-62 relative text-white" style={{ backgroundImage:`url(${image})`, backgroundPosition:'center', backgroundSize:'cover', borderRadius:'20px', display: 'flex', flexDirection: 'column' , marginBottom:'30px'}}>
      <div className="p-4 " style={{ flex: 2, marginTop:'210px' }}>
        <div className="flex justify-between" style={{ marginBottom: '5px' }}>
          <div> 
            <h2>{name}</h2>   
          </div>
          <div>
            <h2>{stars}</h2>
          </div>  
        </div>
        <div className="text-opacity-70 p-7" style={{
          fontSize: '12px',
          border: 'solid 1px white',
          borderRadius: '30px',
          width: '80%',
          padding: '5px'
        }}>
          {profession}
        </div>
      </div>
    </div>
  );
};

export default MentorProfileFrame;
