import React from 'react';
import Navbar from '@/components/ui/navbar';
import BlockHeader from './_blocks/blockHeader';
import BlockAbout from './_blocks/blockAbout';
import BlockSignUp from './_blocks/blockSignUp';
import BlockMentor from './_blocks/blockMentor';
import BlockFooter from './_blocks/blockFooter';

export default function Home ()  {
  return (
    <>
    <BlockHeader/>
    <BlockAbout/>
    <BlockSignUp/>
    <BlockMentor/>
    <BlockFooter/>
    </>
  );
};


