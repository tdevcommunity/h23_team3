import React from 'react';
import FirstSection from '@/components/home-section1/firstSection';
import Navbar from '../components/navbar/navbar';

const Home = () => {
  return (
    <>
      <div className=''>
        <Navbar />
      </div>
      <div className="flex justify-center mt-10"> 
        <FirstSection />
      </div>
    </>
  );
};

export default Home;
