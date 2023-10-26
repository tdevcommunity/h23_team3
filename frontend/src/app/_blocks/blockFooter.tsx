import linksData from '@/data/links.json'
import Link from 'next/link';
import Image from 'next/image'

const BlockFooter = () => {
  return <section className="w-full bg-gray-800 p-6   text-white">
    <div className="w-10/12 mx-auto flex items-center justify-between my-2 pt-8 pb-8 border-b space-x-4 mt-8">
      <div className="flex gap-20">
        <Image
          src="/assets/logo/xmentor-w.svg"
          className="my-2"
          alt="xmentor-logo"
          width={120}
          height={100}
        />
        <ul className="flex gap-10 items-end">
          {linksData.map((link) => (
            <Link className="" href={link.url} passHref key={link.id}>
              {link.name}
            </Link>
          ))}
        </ul>
      </div>
      <div className="flex space-x-4">
        <span className="w-6 h-6 rounded-full bg-gray-300"></span>
        <span className="w-6 h-6 rounded-full bg-gray-300"></span>
        <span className="w-6 h-6 rounded-full bg-gray-300"></span>
      </div>
    </div>

    <div className="flex gap-20 w-10/12 mx-auto flex items-center justify-between    my-2  pt-6" >
      <ul className="flex gap-10  items-end">
        <span>@2023 ElementX</span>
        <Link href={"/termes"}>Termes</Link>
        <Link href={"/politique"}>Politique</Link>
      </ul>
    </div>
  </section>
}

export default BlockFooter;