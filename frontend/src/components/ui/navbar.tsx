"use client"
import Link from 'next/link';
import Image from 'next/image';
import linksData from '@/data/links.json';
import { Key, useEffect } from 'react';
import { Url } from 'url';
import { Button } from './button';
import {LinkButton, LinkButtonCircle} from './linkButton';

const Navbar = () => {
  
  const links: {
    id: Key,
    name: String,
    url:  any,
    target: String
  }[] = linksData;
useEffect(() => {
  document.addEventListener('scroll', () => {
   //  console.log(window.innerHeight > 100 ) ;
  })
  return () => {

  }

},[]) ;
  return (
    <nav className={`p-4 bg-white/80 border-b backdrop-blur-sm fixed w-full`}>
      <div className="w-10/12 mx-auto flex items-center justify-between  duration-300  my-2">
        <div className="flex gap-20 ">
          <Image
            src="/assets/logo/xmentor.svg"
            className="my-2"
            alt="xmentor-logo"
            width={120}
            height={100}
          />
          <ul className="flex gap-10  items-end">
            {links.map(link => <Link className='' href={link.url} passHref key={link.id}> {link.name }</Link>)}
          </ul>
        </div>
        <div className="flex space-x-4 items-center">

        <LinkButtonCircle href="#" target=''>
        Se connecter
        </LinkButtonCircle>
        <LinkButton  href="#" target=''>
          Inscription
        </LinkButton>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
