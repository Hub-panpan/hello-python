package com.itheima12.spring.aop.xml.exception.test;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.itheima12.spring.aop.xml.exception.service.StudentService;

public class ExceptionTest {
	@Test
	public void testException() throws Exception{
		ApplicationContext context = 
				new ClassPathXmlApplicationContext("applicationContext.xml");
//客户端  第一步启动容器
//利用Perservice进行接受   强制转型
		
//这个类最主要的缺点  我不关注你有多少层 
//只要是你使用AOP了我就能获取异常  我放到value stat 中 就能通过ongl 表达式取值出来
//  Spring几乎每个企业都在用 
//		PersonService personService = (PersonService)context.getBean("personService");
//		personService.updatePerson();
		
		StudentService studentService = (StudentService)context.getBean("studentService");
		studentService.savePerson();
	}
}
