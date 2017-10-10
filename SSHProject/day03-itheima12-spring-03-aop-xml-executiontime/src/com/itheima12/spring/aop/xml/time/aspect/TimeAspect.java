package com.itheima12.spring.aop.xml.time.aspect;
//切面方法
import org.aspectj.lang.ProceedingJoinPoint;
import org.omg.CORBA.PUBLIC_MEMBER;

public class TimeAspect {
	//方法名字：方法的执行时间
	public void methodExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable{
		//哪个类的哪个方法  执行的时间
		
		String targetClassName = joinPoint.getTarget().getClass().getName();//得到是哪个类
		String methodName = joinPoint.getSignature().getName();//得到是哪个方法
		
		long preTime = System.currentTimeMillis();//获取到当前时间 毫秒级别 类型是long
		
		joinPoint.proceed();//执行目标类的目标方法
		
		long postTime = System.currentTimeMillis();//再次获得一下系统的时间
		long executionTime = postTime-preTime;//经过的时间
		//选择执行时间 输出一下
		System.out.print("当前的类是:"+targetClassName+",");
		System.out.print("当前的方法是:"+methodName+",");
		System.out.print("当前方法的开始时间:"+preTime+",");
		System.out.println("当前方法的执行时间:"+executionTime);
		
		
		//假设现在想计算出 所有的时间 怎么办呢 
		//1.可以写个javabean 有个属性
	
	}
}
