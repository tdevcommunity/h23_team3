import Link from 'next/link';
import Image from 'next/image';

const Navbar = () => {
  return (
    <nav className="p-4 my-2 mx-2">
      <div className="container mx-auto flex justify-between items-center w-4/5 my-2">
        <div className="flex items-center">
          <Image
            src="/xmentor.svg"
            className="mx-auto"  
            alt="xmentor-logo"
            width={100}
            height={50}
          />
          <ul className="flex space-x-4 ml-10">
            <li>
              <Link href="/">Mentors</Link>
            </li>
            <li>
              <Link href="/">Questions</Link>
            </li>
            <li>
              <Link href="/">Ressources</Link>
            </li>
            <li>
              <Link href="/">Job</Link>
            </li>
            <li>
              <Link href="/">A Propos</Link>
            </li>
          </ul>
        </div>
        <div className="flex space-x-4 items-center">
          <ul>
            <li>
              <Link href="/">Se Connecter</Link>
            </li>
          </ul>
          <ul>
            <li>
              <Link href="/"  >
                <p className="rounded-full bg-purple-500 text-white p-2">Inscription</p>
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
